import Axios from "axios";
import { useEffect, useState } from "react";
import "./networth.css";

function NetWorth({
  currency,
  refresh_networth,
  total_assets,
  total_liabilities,
  currency_symbol,
}) {
  const [networth, getNetWorth] = useState(0);

  console.log("currency at networth: " + currency);

  console.log("reached_here");

  useEffect(() => {
    Axios("http://localhost:8080/my_business/transactions/networth")
      .then((res) => {
        getNetWorth(res.data["networth"] * currency.toFixed(2));
        total_assets(res.data["assets"] * currency.toFixed(2));
        total_liabilities(res.data["liabilities"] * currency.toFixed(2));
      })

      .catch((err) => console.log(err));
  }, [currency, refresh_networth]);

  return (
    <div className="networth">
      <b>NetWorth: </b>
      {currency_symbol}&nbsp;{" "}
      {networth
        .toFixed(2)
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, ",")}
    </div>
  );
}

export default NetWorth;
