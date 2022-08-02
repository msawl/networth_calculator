import logo from "./logo.svg";
import "./App.css";
import Axios from "axios";
import { useEffect, useState } from "react";
import Table from "./components/table";
import NetWorth from "./components/networth";

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

  const changeCurrency = (currency) => {
    Axios.get(
      "http://localhost:8080/my_business/exchangerate/" + currency
    ).then((response) => {
      setCurrency(response.data["rate"]);
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

  return (
    <div className="App">
      <h1>Tracking NetWorth</h1>
      <div className="information">
        <label for="cars">Select Currency:</label>
        <select
          name="currency"
          onChange={(event) => {
            changeCurrency(event.target.value);
          }}
          id="currency"
        >
          <option value="USD">USD</option>
          <option value="CAD">CAD</option>
          <option value="AUD">AUD</option>
          <option value="INR">INR</option>
        </select>
      </div>
      <NetWorth currency={currency} refresh_networth={r_networth} />
      <h3>Asset</h3>
      <Table
        data={dataTable}
        column={column}
        currency_rate={currency}
        oncomplete={toggle_refresh}
      />
      <h3>Liabilities</h3>
      <Table
        data={liabilities}
        column={column}
        currency_rate={currency}
        oncomplete={toggle_refresh}
      />
    </div>
  );
}

export default App;
