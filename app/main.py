# app/main.py
self.debounce_ms = cfg['app'].get('debounce_ms', 6)
self.poll_period = 1.0 / cfg['app'].get('pressure_poll_hz', 200)
self.last_state = False
self.last_change = 0.0


def run(self):
self.log.info("Pressure thread started")
while not STOP.is_set():
val = self.sensor.read()
now = time.time()
state = val >= self.threshold
# Debounce transitions
if state != self.last_state and (now - self.last_change) * 1000 >= self.debounce_ms:
self.last_state = state
self.last_change = now
evt = make_pressure_event(value=val, pressed=state)
self.out_q.put(evt)
time.sleep(self.poll_period)
self.log.info("Pressure thread stopped")




class AudioThread(threading.Thread):
def __init__(self, cfg, out_q: queue.Queue):
super().__init__(daemon=True)
self.log = logging.getLogger('AudioThread')
self.cfg = cfg
self.out_q = out_q
self.capture = AudioCapture(
sample_rate=cfg['app'].get('sample_rate_hz', 16000),
frame_ms=cfg['app'].get('frame_ms', 30),
vad_aggr=cfg['app'].get('vad_aggressiveness', 2),
base_dir=cfg['app'].get('local_audio_dir', '/var/lib/pen/audio')
)


def run(self):
self.log.info("Audio thread started")
for audio_evt in self.capture.stream(STOP):
# audio_evt has keys: path, start_ts, end_ts, duration_s
evt = make_audio_event(audio_evt)
self.out_q.put(evt)
self.log.info("Audio thread stopped")




def build_uplink(cfg):
mode = cfg['uplink'].get('mode', 'mqtt')
if mode == 'mqtt':
return MQTTClient(cfg)
elif mode == 'https':
return HTTPSClient(cfg)
else:
raise ValueError(f"Unknown uplink mode: {mode}")




class UplinkThread(threading.Thread):
def __init__(self, cfg, in_q: queue.Queue, lq: LocalQueue):
super().__init__(daemon=True)
self.log = logging.getLogger('UplinkThread')
self.cfg = cfg
self.in_q = in_q
self.lq = lq
self.client = build_uplink(cfg)


def run(self):
self.log.info("Uplink thread started")
while not STOP.is_set():
try:
# Drain in-memory queue quickly
try:
evt = self.in_q.get(timeout