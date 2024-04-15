import "./App.css";
import React from "react";


let name = "Hariom Singh Rajput";

function App() {
  return (
    // React Fragment - It eliminate the default div create by react
    <React.Fragment>
      <nav>
        <li>Home</li>
        <li>Services</li>
        <li>About</li>
        <li>Contact</li>
      </nav>

      <div className="container">
        <h1>React JS with {name}</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus ex possimus sed libero corrupti vitae quam sapiente repellat exercitationem porro eius consequatur quos necessitatibus nobis, fugiat delectus quaerat accusantium praesentium aperiam unde ipsam aut culpa nisi. Nisi, fugit nobis autem, ab iusto corporis repellat deserunt aliquid magnam asperiores error ut aliquam vitae eaque culpa, ducimus harum sequi expedita porro quod eos? Ipsa nostrum excepturi totam aspernatur sequi nobis? Blanditiis deserunt sequi voluptate explicabo tempora modi! Harum obcaecati culpa tempore. Nisi, consequatur. Numquam provident enim tempore? Placeat dolorem, aliquam animi illum accusamus mollitia dolores ad, eligendi id distinctio beatae? Odit, quis!</p>
      </div>
    </React.Fragment>

    // It is another short way to use React Fragment
    // <>
    //   <nav>
    //     <li>Home</li>
    //     <li>Services</li>
    //     <li>About</li>
    //     <li>Contact</li>
    //   </nav>

    //   <div className="container">
    //     <h1>React JS with {name}</h1>
    //     <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus ex possimus sed libero corrupti vitae quam sapiente repellat exercitationem porro eius consequatur quos necessitatibus nobis, fugiat delectus quaerat accusantium praesentium aperiam unde ipsam aut culpa nisi. Nisi, fugit nobis autem, ab iusto corporis repellat deserunt aliquid magnam asperiores error ut aliquam vitae eaque culpa, ducimus harum sequi expedita porro quod eos? Ipsa nostrum excepturi totam aspernatur sequi nobis? Blanditiis deserunt sequi voluptate explicabo tempora modi! Harum obcaecati culpa tempore. Nisi, consequatur. Numquam provident enim tempore? Placeat dolorem, aliquam animi illum accusamus mollitia dolores ad, eligendi id distinctio beatae? Odit, quis!</p>
    //   </div>

    // </>
  );
}

export default App;
