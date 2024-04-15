const mongoose = require("mongoose");

// For local database
// const URI = "mongodb://127.0.0.1:27017/mern_admin";

// For actual database
const URI = process.env.MONGODB_URI;

// mongoose.connect(URI);

const connectDb = async () => {
  try {
    await mongoose.connect(URI);
    console.log("MongoDB connected successfully...");
  } catch (error) {
    console.error("Database connection failed!");
    process.exit(0);
  }
};

module.exports = connectDb;