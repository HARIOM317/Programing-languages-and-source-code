import React, {useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";

const StateWise = () => {
  const [data, setData] = useState([]);

  const getCovidData = async () => {
    const res = await fetch("https://api.covid19india.org/data.json");
    const actualData = await res.json();
    console.log(actualData.statewise);
    setData(actualData.statewise);
  };

  // It will automatically call during render method call
  useEffect(() => {
    getCovidData();
  }, []);

  return (
    <>
      <div className="container mt-5">
        <div className="main-heading">
          <h1 className="mb-5 text-center">
            <span className="fw-bold">INDIA </span> COVID-19 Dashboard
          </h1>
        </div>

        <div className="table-responsive">
          <table className="table table-hover">
            <thead className="table-dark">
              <tr>
                <th>State</th>
                <th>Confirmed</th>
                <th>Recovered</th>
                <th>Deaths</th>
                <th>Active</th>
                <th>Last Update Time</th>
              </tr>
            </thead>

            <tbody>
              {data.map((element, index) => {
                return (
                  <tr key={index}>
                    <td>{element.state}</td>
                    <td>{element.confirmed}</td>
                    <td>{element.recovered}</td>
                    <td>{element.deaths}</td>
                    <td>{element.active}</td>
                    <td>{element.lastupdatedtime}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
};

export default StateWise;
