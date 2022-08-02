import Axios from "axios";
import { useEffect, useState } from "react";
import "./networth.css";

function NetWorth({ currency, refresh_networth }) {
  const [networth, getNetWorth] = useState("");

  console.log("currency at networth: " + currency);

  console.log("reached_here");

  useEffect(() => {
    Axios("http://localhost:8080/my_business/transactions/networth")
      .then((res) => getNetWorth(res.data["networth"] * currency.toFixed(2)))
      .catch((err) => console.log(err));
  }, [currency, refresh_networth]);

  return (
    <div className="networth">
      <h3>NetWorth:</h3>
      <p>{networth}</p>
    </div>
  );
}

export default NetWorth;
