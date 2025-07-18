#!/usr/bin/env node
import express from "express";
import multer from "multer";

const app = express();

app.use(express.urlencoded({ extended: false }));
app.use(multer().none());

app.post("/create_user", (req, res) => {
  console.log("Creating user:");
  console.log(req.headers["content-type"]);
  console.log(req.body);

  res.send("OK");
});

app.listen(9501);
