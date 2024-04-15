import "./App.css";
// import About from "./components/About";
import Navbar from "./components/Navbar";
import TextForm from "./components/TextForm";

function App() {
  return (
    <>
      <Navbar title="State Handling Events" />
      <div className="container my-3">
        <TextForm heading="Please Fill This Form" />
        {/* <About/> */}
      </div>
    </>
  );
}

export default App;

