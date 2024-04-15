const User = require("../models/user-model");
const bcrypt = require("bcryptjs");

// Home controller
const home = async (req, res) => {
  try {
    res.status(200).send("Welcome Friends!");
  } catch (error) {
    console.log(error);
  }
};

// ===== Register controller (User Registration Logic) =====
const register = async (req, res) => {
  try {
    // console.log(req.body);
    const { username, email, phone, password } = req.body;

    const userExist = await User.findOne({ email: email });

    // Checking if user already exist or not
    if (userExist) {
      return res.status(400).json({ msg: "email already exists!" });
    }

    //  Creating new user and saving it to the database
    const userCreated = await User.create({
      username,
      email,
      phone,
      password,
    });

    res.status(201).json({
      msg: "Registration Successful",
      token: await userCreated.generateToken(),
      userId: userCreated._id.toString(),
    });
  } catch (error) {
    res.status(500).json("Internal server error!");
  }
};

// ===== Login controller (User Login Logic) =====
const login = async (req, res) => {
  try {
    const { email, password } = req.body;
    const userExist = await User.findOne({ email: email });
    console.log(userExist);

    if (!userExist) {
      return res.status(400).json({ message: "Invalid Credentials" });
    }

    // comparing password
    const user = await bcrypt.compare(password, userExist.password);

    if (user) {
      res.status(200).json({
        msg: "Login Successful",
        token: await userExist.generateToken(),
        userId: userExist._id.toString()
      });
    } else {
      res.status(401).json({ massage: "Invalid email or password" });
    }
  } catch (error) {
    res.status(500).json("Internal server error!");
  }
};

module.exports = { home, register, login };
