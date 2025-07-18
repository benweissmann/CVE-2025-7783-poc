import express from "express";
import FormData from "form-data";

const BACKEND_API = "http://localhost:9501/create_user";

const app = express();

app.use(express.urlencoded({ extended: false }));

app.get("/example", (req, res) => {
  res.header(
    "x-request-id",
    `${Math.floor(Math.random() * 1e11)}`.padStart(11, "0")
  );
  res.send("Example");
});

app.post("/invite_user", (req, res) => {
  let name = req.body.name;

  let data = new FormData();
  data.append("name", name);

  data.submit(BACKEND_API, (err, response) => {
    if (err) {
      console.log(err);
      res.status(500).send("Error");
    } else {
      console.log(response.statusCode);
      res.send("OK");
    }
  });
});

app.listen(9500);
