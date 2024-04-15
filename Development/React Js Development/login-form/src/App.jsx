import React, { useState } from "react";
import "./index.css";

const App = () => {
  const [data, setData] = useState({
    name: "",
    address: "",
    email: "",
    phone: "",
    password: "",
  });

  const changeData = (event) => {
    const value = event.target.value;
    const name = event.target.name;

    setData((prevValue) => {
      // if (name === "name") {
      //   return {
      //     name: value,
      //     email: prevValue.email,
      //     phone: prevValue.phone,
      //     address: prevValue.address,
      //     password: prevValue.password,
      //   };
      // } else if (name === "address") {
      //   return {
      //     name: prevValue.name,
      //     email: prevValue.email,
      //     phone: prevValue.phone,
      //     address: value,
      //     password: prevValue.password,
      //   };
      // } else if (name === "email") {
      //   return {
      //     name: prevValue.name,
      //     email: value,
      //     phone: prevValue.phone,
      //     address: prevValue.address,
      //     password: prevValue.password,
      //   };
      // } else if (name === "phone") {
      //   return {
      //     name: prevValue.name,
      //     email: prevValue.email,
      //     phone: value,
      //     address: prevValue.address,
      //     password: prevValue.password,
      //   };
      // } else if (name === "password") {
      //   return {
      //     name: prevValue.name,
      //     email: prevValue.email,
      //     phone: prevValue.phone,
      //     address: prevValue.address,
      //     password: value,
      //   };
      // }

      // Short way using spread operator (...name)
      return {
        ...prevValue,
        [name]: value,
      };
      
    });
  };

  const submitForm = (event) => {
    event.preventDefault();
    alert("Form Submitted Successfully!");
  };

  return (
    <>
      <div>
        <form onSubmit={submitForm}>
          <div>
            <div className="details">
              <h1>{data.name}</h1>
              <h1>{data.email}</h1>
              <h1>{data.phone}</h1>
              <h1>{data.address}</h1>
            </div>

            <input
              type="text"
              placeholder="Enter Your Name"
              onChange={changeData}
              name="name"
              value={data.name}
              required
            />
            <input
              type="email"
              placeholder="Enter Your Email"
              onChange={changeData}
              name="email"
              value={data.email}
              required
            />
            <input
              type="phone"
              placeholder="Enter Your Phone"
              onChange={changeData}
              name="phone"
              value={data.phone}
              required
            />
            <input
              type="text"
              placeholder="Enter Your Address"
              onChange={changeData}
              name="address"
              value={data.address}
              required
            />
            <input
              type="password"
              placeholder="Enter Your Password"
              onChange={changeData}
              name="password"
              value={data.password}
              required
            />
            <button type="submit">Submit</button>
          </div>
        </form>
      </div>
    </>
  );
};

export default App;
