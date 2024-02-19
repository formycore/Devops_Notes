import requests

filenames = """
    absint-astree
    accelerated-build-now-plugin
    """

for i in filenames.split():
    url = f"https://updates.jenkins.io/latest/{i}.hpi"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{i}.hpi", 'wb') as f:
            f.write(response.content)
        print(f"File downloaded: {i}.hpi")
    else:
        print(f"File {i}.hpi not found")
