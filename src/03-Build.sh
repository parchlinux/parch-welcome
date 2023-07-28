#!/usr/bin/env bash

echo "#!/usr/bin/python" > Welcome
cat Res.py >> Welcome
cat Welcome.py >> Welcome
chmod +x Welcome
cp Welcome ../rootcopy/usr/bin/