const { MongoClient } = require("mongodb");

const uri = "mongodb://127.0.0.1";

const client = new MongoClient(uri);

const data1 = {
  name: "Hariom Singh Rajput",
  company: "Microsoft",
  price: 5000000,
  colors: ["Red", "Blue", "Yellow", "Green"],
  image: "/images/product.png",
  category: "64c2342de32f4a51b19b9250",
  isFeatured: true,
};

const main = async () => {
  await client.connect();
  const db = client.db("shop");
  const collection = db.collection("products");

  //   Inserting data
  await collection.insertOne(data1);

  //   Fetching data
  const data = await collection.find({ price: { $eq: 5000000 } }).toArray();
  console.log(data);
  return "done";
};

main()
  .then(console.log("Successfully Done!"))
  .catch((e) => console.log(`Error: ${e}`))
  .finally(() => client.close());
