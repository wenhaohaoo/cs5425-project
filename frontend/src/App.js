import React, {useEffect, useRef, useState} from 'react'
import './App.css';
import DatePicker from "./DatePicker";
import PlotChart from "./PlotChart";
import AggregatedSentiments from "./AggregatedSentiments";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from "axios";
import keyCovidEventsSingapore from "./KeyCovidEventsSingapore";
import keyCovidEventsAustralia from "./KeyCovidEventsAustralia";
import keyCovidEventsHongKong from "./KeyCovidEventsHongKong";

const App = () => {

  const [data, setData] = useState()
  const [policiesData, setPoliciesData] = useState([])


  const setCountryPoliciesData = (country) => {
      switch (country) {
          case 'sg':
              setPoliciesData(keyCovidEventsSingapore)
              break;
          case 'au':
              setPoliciesData(keyCovidEventsAustralia)
              break;
          case 'hk':
              setPoliciesData(keyCovidEventsHongKong)
              break;
          default:
              setData([])
      }
  }

  const restApiCallGetData = async (startDate, endDate, country) => {

      //Node and NPM version
      //npm version: 8.3.0
      //node: 16.6.2

      //Will need your help to liaise with wen hao on the below
      //1) The data retrieved from the backend should ideally be ordered by date
      //2) The data format is an array of JSON.
      //3) Clarify on the URL

      //Build URL String
      let URL = 'http://localhost:5000/sentiment/' + country + '?start=' +startDate + '&end=' + endDate
      await axios.get(URL).then(res => {
          res.data.forEach((item)=>{
              item.positive *=100
              item.negative *=100
            })
         // res.data.forEach((item)=>item.negative *=100)
          setData(res.data)
        })
        
      setCountryPoliciesData(country)
  }

    const showPolicies = (country) => {
        if (policiesData.length == 0) {
            setCountryPoliciesData(country)
        }else {
            setPoliciesData([])
        }
    }

  return (
    <div className="App">
        <h1>Visualization of Trends Around Covid-Related Policies</h1>
        <AggregatedSentiments></AggregatedSentiments>
        <DatePicker dataChangeController = {restApiCallGetData} showPolicies = {showPolicies}></DatePicker>
        <PlotChart chartData = {data} policiesData = {policiesData}></PlotChart>
    </div>
  );
}

export default App;
