import React, { useEffect, useState } from "react";

const Covid = () => {
    const [data, setData] = useState([]);

  const getCovidData = async () => {
    try {
      const res = await fetch(
        "https://data.covid19india.org/v4/min/data.min.json"
      );
      const actualData = await res.json();
      console.log(actualData['MP'].total);
      setData(actualData["MP"].total);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    getCovidData();
  }, []);

  return (
    <div className="container">
      <div class="py-5 text-center">
        <h2>🔴 LIVE - MADHYA PRADESH</h2>
        <p class="lead">COVID-19 CORONAVIRUS TRACKER</p>
      </div>

      {/* Cards */}
      <div className="card w-50 container my-4 bg-dark">
        <div className="card-body">
          <h5 className="card-title text-warning">MADHYA PRADESH</h5>
          <h4 className="card-title text-info">TOTAL CONFIRMED</h4>
          <p className="card-text text-light">{data.confirmed}</p>
        </div>
      </div>

      <div className="card w-50 container my-4 bg-dark">
        <div className="card-body">
          <h5 className="card-title text-warning">MADHYA PRADESH</h5>
          <h4 className="card-title text-info">TOTAL DECEASED</h4>
          <p className="card-text text-light">{data.deceased}</p>
        </div>
      </div>

      <div className="card w-50 container my-4 bg-dark">
        <div className="card-body">
          <h5 className="card-title text-warning">MADHYA PRADESH</h5>
          <h4 className="card-title text-info">TOTAL RECOVERED</h4>
          <p className="card-text text-light">{data.recovered}</p>
        </div>
      </div>

      <div className="card w-50 container my-4 bg-dark">
        <div className="card-body">
          <h5 className="card-title text-warning">MADHYA PRADESH</h5>
          <h4 className="card-title text-info">TOTAL TESTED</h4>
          <p className="card-text text-light">{data.tested}</p>
        </div>
      </div>

      <div className="card w-50 container my-4 bg-dark">
        <div className="card-body">
          <h5 className="card-title text-warning">MADHYA PRADESH</h5>
          <h4 className="card-title text-info">TOTAL VACCINATED 1</h4>
          <p className="card-text text-light">{data.vaccinated1}</p>
        </div>
      </div>

      <div className="card w-50 container my-4 bg-dark">
        <div className="card-body">
          <h5 className="card-title text-warning">MADHYA PRADESH</h5>
          <h4 className="card-title text-info">TOTAL VACCINATED 2</h4>
          <p className="card-text text-light">{data.vaccinated2}</p>
        </div>
      </div>
    </div>
  );
};

export default Covid;
