import subprocess

import subprocess

# فتح عملية
process = subprocess.Popen(["echo", "Hello from Popen"], stdout=subprocess.PIPE, text=True)

# قراءة النتيجة
output, _ = process.communicate()

print("Output:", output)

