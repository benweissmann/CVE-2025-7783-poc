# form-data boundary randomness vulnerability (CVE-2025-7783)

Largely based on https://hackerone.com/reports/2913312 by https://hackerone.com/parrot409?type=user

Installing:
- `npm install`
- Make sure you have `python3` installed with the `z3` module (`pip3 install -r requirements.txt`) -- the exploit code shells out to `python3` to predict the next random value

Running:

In parallel, run:
- `npm run start-backend` (the backend server that will receive the manipulated request)
- `npm run start-vulnerable-server` (the frontend server that can be tricked into sending a manipulated request)
- `npm run exploit` (the client code that crafts and sends the exploit)

In the stdout of `npm run backend`, you should see a request with `is_admin: true` (despite the code in `vulnerable-server.js` never intending to add an is_admin parameter to the API call)
