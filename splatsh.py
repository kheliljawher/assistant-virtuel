import requests

script = """
splash:go(args.url)
return splash:png()
"""
resp = requests.post('http://localhost:8050/run', json={
    'lua_source': script,
    'url': 'http://example.com'
})
png_data = resp.content