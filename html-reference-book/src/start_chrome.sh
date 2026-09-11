#!/bin/sh
# Starts a headless Chrome (from the @sparticuz/chromium npm package) with a DevTools endpoint on port 9333.
# Setup once:  cd /tmp && npm pack @sparticuz/chromium && mkdir chr && tar xzf sparticuz-chromium-*.tgz -C chr
#              then decompress the .br files in chr/package/bin (see render_shots.py header).
B=${CHROME_BIN_DIR:-/tmp/chr/package/bin}
cd "$B" && LD_LIBRARY_PATH=$B/lib:$B exec ./chromium --headless=new --no-sandbox --disable-gpu --no-zygote \
  --disable-dev-shm-usage --user-data-dir=/tmp/chrome-profile --remote-debugging-port=9333 --remote-allow-origins=* \
  --font-render-hinting=none about:blank
