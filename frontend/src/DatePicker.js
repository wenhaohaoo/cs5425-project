import React, {useEffect, useState} from 'react'
import {Button, Col, FloatingLabel, Form, Row} from 'react-bootstrap';
import './DatePicker.css'

let Countries = ["Singapore" , "Australia" , "Hong Kong"]

function GenerateSelectValueForCountries(){
    let generatedOption = Countries.map(function (country, i) {
        return (<option key={i} value = {country}> {country}</option>)
    })
    return generatedOption
}

const DatePicker = (props) => {

    const [startDate , setStartDate] = useState()
    const [endDate, setEndDate] = useState()
    const [country, setCountry] = useState("sg")

    const formSubmit = (event) => {
        event.preventDefault();
        console.log(startDate, endDate, country)
        props.dataChangeController(startDate, endDate, country)
    }

    const handleDateChange = (event) => {
        event.preventDefault()
        if (event.target.name === "startDate") {
            setStartDate(event.target.value)
        }else {
            setEndDate(event.target.value)
        }
    }

    const handleCountryChange = (event) => {
        if(event.target.value == 'Australia') {
            setCountry("au")
        } else if(event.target.value == 'Hong Kong') {
            setCountry("hk")
        } else {
            setCountry("sg")
        }
    }

    return (
        <div className="datePicker">
            <Form className="datePickerForm">
                <Row className="g-2 mb-4">
                    <Col>
                        <FloatingLabel controlId="floatingInputGrid" label="Start Date">
                            <Form.Control max={new Date().toISOString().split("T")[0]} type="date" name="startDate" placeholder="startDate" onChange = {handleDateChange}/>
                        </FloatingLabel>
                    </Col>
                    <Col style = {{marginLeft: '10px' , marginRight: '10px'}}>
                        <FloatingLabel controlId="floatingInputGrid" label="End Date">
                            <Form.Control max={new Date().toISOString().split("T")[0]} type="date" name="endDate" placeholder="endDate" onChange = {handleDateChange}/>
                        </FloatingLabel>
                    </Col>
                    <Col >
                        <FloatingLabel controlId="floatingSelectGrid" label="Country">
                            <Form.Select aria-label="Floating label select example" name="Countries" onChange={handleCountryChange} >
                                <GenerateSelectValueForCountries  />
                            </Form.Select>
                        </FloatingLabel>
                    </Col>
                </Row>
                <Button variant ="secondary" size = "lg" type = 'submit' onClick = {formSubmit} style ={{width: '20%'}}>Submit</Button>
            </Form>
            <Form.Check aria-label="option 1" label = "Show Policies" style = {{marginTop: '10px'}} onClick={() => props.showPolicies(country)} isValid={false}/>
        </div>
    )
}

export default DatePicker