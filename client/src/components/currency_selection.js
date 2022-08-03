import Axios from "axios";
import { useEffect, useState } from "react";

function CurrencySelector({ selection }) {
  return (
    <div className="information">
      <label for="cars">Select Currency:</label>
      <select
        name="currency"
        onChange={(event) => {
          selection(event.target.value);
        }}
        id="currency"
      >
        <option value="USD">USD</option>
        <option value="CAD">CAD</option>
        <option value="AUD">AUD</option>
        <option value="INR">INR</option>
        <option value="HKD">HKD</option>
        <option value="GBP">GBP</option>
        <option value="SGD">SGD</option>
        <option value="JPY">JPY</option>
        <option value="EUR">EUR</option>
        <option value="AED">AED</option>
      </select>
    </div>
  );
}

export default CurrencySelector;
