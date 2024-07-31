const Card = ({ children }: { children: React.ReactNode }) => {
  const cardStyle = {
    padding: "100px 200px",
    margin: "10px",
    boxShadow: "0 4px 8px 0 rgba(0, 0, 0, 0.2)",
    border: "1.5px solid gray",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    gap: "2rem",
    borderRadius: "8px",
    background: "#1c212f",
    width: "100%",
  };

  return <div style={cardStyle}>{children}</div>;
};

export default Card;
