import logo from "./logo.svg";
import "./App.css";
import Axios from "axios";
import { useEffect, useState } from "react";
import Table from "./components/table";
import NetWorth from "./components/networth";
import CurrencySelector from "./components/currency_selection.js";

function App() {
  const [dataTable, setDataTable] = useState([]);
  const [liabilities, setLiabilities] = useState([]);
  console.log(dataTable);
  useEffect(() => {
    Axios("http://localhost:8080/my_business/transactions")
      .then((res) => {
        setDataTable(res.data["results"]["assets"]);
        setLiabilities(res.data["results"]["liabilities"]);
      })
      .catch((err) => console.log(err));
  }, []);

  const [currency, setCurrency] = useState(1);
  const [currency_symbol, setCurrency_symbol] = useState("USD");

  const changeCurrency = (currency) => {
    Axios.get(
      "http://localhost:8080/my_business/exchangerate/" + currency
    ).then((response) => {
      setCurrency(response.data["rate"]);
      setCurrency_symbol(currency);
    });
  };

  const [r_networth, refresh_networth] = useState(false);

  const toggle_refresh = () => {
    refresh_networth(!r_networth);
  };

  const column = [
    { heading: "Holdings", value: "name_of_holding" },
    { heading: "Amount", value: "amount" },
    { heading: "id", value: "id" },
  ];

  const [totalAssets, getTotalAssets] = useState(0);
  const [totalLiabilities, getTotalLiabilities] = useState(0);

  return (
    <div className="App">
      <h1>Tracking NetWorth</h1>
      <CurrencySelector selection={changeCurrency} />
      <NetWorth
        currency={currency}
        refresh_networth={r_networth}
        total_assets={getTotalAssets}
        total_liabilities={getTotalLiabilities}
      />
      <h3>Assets</h3>
      <Table
        data={dataTable}
        column={column}
        currency_rate={currency}
        oncomplete={toggle_refresh}
        currency_symbol={currency_symbol}
      />
      <div className="totals">Total Assets: {totalAssets}</div>
      <h3>Liabilities</h3>
      <Table
        data={liabilities}
        column={column}
        currency_rate={currency}
        oncomplete={toggle_refresh}
        currency_symbol={currency_symbol}
      />
      <div className="totals">Total Liabilities: {totalLiabilities}</div>
    </div>
  );
}

export default App;
