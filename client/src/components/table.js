import "./table.css";
import Axios from "axios";
import NetWorth from "./networth";
function Table({ data, column, currency_rate, oncomplete, currency_symbol }) {
  return (
    <table>
      <thead>
        <tr>
          {column.map((item, index) => (
            <TableHeadItem item={item} />
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <TableRow
            item={item}
            column={column}
            currency_rate={currency_rate}
            oncomplete={oncomplete}
            currency_symbol={currency_symbol}
            style_left={{ "text-align": "left", width: "50%" }}
            style_right={{ "text-align": "right", width: "25%" }}
          />
        ))}
      </tbody>
    </table>
  );
}

const TableHeadItem = ({ item }) => {
  //   <th>{item.heading}</th>;
  console.log(item.heading);
  if (item.heading != "id") {
    return <th>{item.heading}</th>;
  }
};

const changeData = (event, oncomplete) => {
  if (event.key === "Enter") {
    event.preventDefault();
    Axios.patch(
      "http://localhost:8080/my_business/transactions/" +
        event.target.attributes.dataValue.value,
      {
        amount: event.target.innerText,
      }
    ).then((response) => {
      console.log("success", response.data);
      oncomplete();
    });
  }
};

const TableRow = ({
  item,
  column,
  currency_rate,
  oncomplete,
  currency_symbol,
  style_left,
  style_right,
}) => (
  <tr>
    {column.map((columnItem, index) => {
      if (columnItem.heading != "id") {
        if (index == 1) {
          return (
            <td style={style_right}>
              {currency_symbol} &nbsp;
              <text
                contentEditable="true"
                onKeyDown={(e) => changeData(e, oncomplete)}
                dataValue={item["id"]}
              >
                {(item[`${columnItem.value}`] * currency_rate).toFixed(2)}
              </text>
            </td>
          );
        }

        return <td style={style_left}>{item[`${columnItem.value}`]}</td>;
      }
    })}
  </tr>
);

export default Table;
