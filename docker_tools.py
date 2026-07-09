import subprocess

def list_containers():
    result = subprocess.run(
        ["docker", "ps", "-a"],
        capture_output=True,
        text=True
    )
    return result.stdout


def start_nginx():
    result = subprocess.run(
        ["docker", "start", "my-nginx"],
        capture_output=True,
        text=True
    )
    return result.stdout if result.stdout else result.stderr


def stop_container(name):
    result = subprocess.run(
        ["docker", "stop", name],
        capture_output=True,
        text=True
    )
    return result.stdout if result.stdout else result.stderr