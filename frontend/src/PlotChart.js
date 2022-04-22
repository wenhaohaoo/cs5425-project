import React from "react";
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ReferenceLine
} from "recharts";
import './PlotChart.css'

const PlotChart = (props) => {
    return (
        <div className = "plotchart">
            <LineChart
                width={1450}
                height={650}
                data={props.chartData}
                style = {{marginLeft: 'auto' , marginRight: 'auto'}}
            >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                {
                    props.policiesData.map(function (data , index){
                        let splittedData = data.split(":")
                        return (<ReferenceLine key = {index} x = {splittedData[0]} stroke = "red" label = {splittedData[1]}/>)
                    })
                }
                <Line type="monotone" dataKey="negative" stroke="#8884d8" />
                <Line type="monotone" dataKey="positive" stroke="#82ca9d" />
            </LineChart>
        </div>
    );
}

export default PlotChart