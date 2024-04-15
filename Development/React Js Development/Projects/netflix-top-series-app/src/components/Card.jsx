import React from "react";

function Card(props) {
  return (
    <>
      <div className="cards">
        <div className="card">
          <img src={props.imgSrc} alt="myPic" className="card-img" />
          <div className="card-info">
            <span className="card-category">{props.category}</span>
            <h3 className="card-title">{props.title}</h3>
            <a href={props.link}>
              <button>Watch Now</button>
            </a>
          </div>
        </div>
      </div>
    </>
  );
}

export default Card;