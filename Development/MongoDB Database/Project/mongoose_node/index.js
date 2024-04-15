const mongoose = require("mongoose");

// Foe local database
// const uri = "mongodb://127.0.0.1/shop";

// Foe actual database
const uri =
  "mongodb+srv://hariommewada:Hariom484@cluster0.ivjugfw.mongodb.net/shop?retryWrites=true&w=majority";

mongoose.connect(uri);

// Creating Schema
const productSchema = new mongoose.Schema({
  name: String,
  company: String,
  price: Number,
  colors: [String],
  image: String,
  category: String,
  isFeatured: Boolean,
});

// Creating a Model (Pass collection name in singular form because when it go on database then it automatically becomes plural)
const product = new mongoose.model("product", productSchema);

const data1 = {
  name: "HSR",
  company: "HSR Foundation",
  price: 150000000,
  colors: ["Green", "SkyBlue", "Purple"],
  image: "/images/product.png",
  category: "64c234de32f4a51b19b9250",
  isFeatured: true,
};

const main = async () => {
  // CRUD Operation
  try {
    // 1. Insert document
    await product.insertMany(data1);

    // 2. Read data
    const data = await product.find({ price: { $eq: 150000000 } }).limit(1);
    console.log(data);

    // 3. Update data
    await product.findOneAndUpdate(
      { name: "HSR", price: 150000000 },
      { $set: { price: 100009 } }
    );
    const updatedData = await product.find({ price: { $eq: 100009 } }).limit(1);
    console.log("\n\n===== After Updating ===== \n\n");
    console.log(updatedData);

    // 4. Delete data
    await product.findOneAndDelete({ name: "HSR", price: 100009 });
  } catch (error) {
    console.log(`Error: ${error}`);
  } finally {
    mongoose.connection.close();
  }
};

main();
