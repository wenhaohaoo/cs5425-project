import React, {useEffect, useState} from "react";
import {Button, Card, Col, FloatingLabel, Form, Placeholder, Row} from "react-bootstrap";
import './AggregatedSentiments.css'
import axios from "axios";

let emptyStart = {date: "" , positive: 0 , negative: 0, tweet_count: 0}
let Countries = ["Singapore" , "Australia" , "Hong Kong"]

function GenerateSelectValueForCountries(){
    let generatedOption = Countries.map(function (country, i) {
        return (<option key={i} value = {country}> {country}</option>)
    })
    return generatedOption
}

const AggregatedSentiments = () => {

    const [data7Days , setData7Days] = useState(emptyStart)
    const [data24Hours , setData24Hours] = useState(emptyStart)
    const [data30Days , setData30Days] = useState(emptyStart)
    const [country , setCountryData] = useState("sg")
    const [polling , setPolling] = useState(0)

    const updateData = async (URL_24Hours , URL_7Days , URL_30Days) => {
        await axios.get(URL_24Hours).then(res => {
            res.data.negative = (res.data.negative * 100).toFixed(2)
            res.data.positive = (res.data.positive * 100).toFixed(2)
            setData24Hours(res.data)
        })
        await axios.get(URL_7Days).then(res => {
            res.data.negative = (res.data.negative * 100).toFixed(2)
            res.data.positive = (res.data.positive * 100).toFixed(2)
            setData7Days(res.data)
        })
        await axios.get(URL_30Days).then(res => {
            res.data.negative = (res.data.negative * 100).toFixed(2)
            res.data.positive = (res.data.positive * 100).toFixed(2)
            setData30Days(res.data)
        })

        //------------dummy flow - please delete after backend integration-----------------
        // let _7days = {date: "2021-01-31", positive: 40.6, negative: 59.4, tweet_count: 1000}
        // let _30days = {date: "2021-01-31", positive: 40.6, negative: 59.4, tweet_count: 1000}
        // let _24Hours = {date: "2021-01-31", positive: 40.6, negative: 59.4, tweet_count: 1000}
        // console.log(country)
        // setData7Days(_7days)
        // setData24Hours(_24Hours)
        // setData30Days(_30days)
        //--------------------------------------------------------------
    }

    // useEffect(() => {
    //     const pollingInterval = setInterval(async () => {
    //         let URL_24Hours = 'http://localhost:5000/sentiment/'+ country + '/past-24hr'
    //         let URL_7Days = 'http://localhost:5000/sentiment/'+ country + '/past-7-days'
    //         let URL_30Days = 'http://localhost:5000/sentiment/' + country + '/past-30-days'
    //         await updateData(URL_24Hours , URL_7Days , URL_30Days)
    //         //await updateData("1" , "2" , "3") //remove this line after backend integration
    //         setPolling(prevState => prevState + 1)
    //     }, 300000) // Update every 300 seconds -> polling

    //     return () => clearInterval(pollingInterval)

    // } , [polling])


    const handleCountryChange = (event) => {
        if(event.target.value == 'Singapore') {
            setCountryData('sg')
        }
        else if(event.target.value == 'Hong Kong') {
            setCountryData('hk')
        } 
    }

    const sendURL = async(event) => {
        let URL_24Hours = 'http://localhost:5000/sentiment/'+ country + '/past-24hr'
        let URL_7Days = 'http://localhost:5000/sentiment/'+ country + '/past-7-days'
        let URL_30Days = 'http://localhost:5000/sentiment/' + country + '/past-30-days'
        await updateData(URL_24Hours , URL_7Days , URL_30Days)
    }

    const formSubmit = async(event) => {
             let URL_24Hours = 'http://localhost:5000/sentiment/'+ country + '/past-24hr'
       let URL_7Days = 'http://localhost:5000/sentiment/'+ country + '/past-7-days'
        let URL_30Days = 'http://localhost:5000/sentiment/' + country + '/past-30-days'
        await updateData(URL_24Hours , URL_7Days , URL_30Days)
        //await updateData("1" , "2" , "3") 
    }


    return (
        <React.Fragment>
            <Form className = 'sentimentForm'>
                <Row className="g-2 mb-4">
                    <Col >
                        <FloatingLabel controlId="floatingSelectGrid" label="Country">
                            <Form.Select aria-label="Floating label select example" name="Countries" onChange={handleCountryChange} >
                                <GenerateSelectValueForCountries  />
                            </Form.Select>
                        </FloatingLabel>
                    </Col>
                </Row>
                <Row className="g-2 mb-4">
                    <Col>
                     <Button variant ="secondary" size = "lg" onClick = {sendURL} style ={{width: '100%'}}>Proceed</Button>
                    </Col>
                </Row>
            </Form>
            <div className="d-flex justify-content-center">
                <Card className = 'cardDesign'>
                    <Card.Body>
                        <Card.Title >Past <span className = "text">7</span> days</Card.Title>
                        <Card.Text>
                                <p className = "score score-green">{'+' + data7Days.positive}</p>
                                <p className = "score-green">positive</p>
                                <p className = "score score-red">{'-' + data7Days.negative}</p>
                                <p className = "score-red">negative</p>
                                <p>Out of <span className = "text">{data7Days.tweet_count}</span> tweets</p>
                        </Card.Text>
                    </Card.Body>
                </Card>
                <Card className = 'cardDesign'>
                    <Card.Body>
                        <Card.Title >Past <span className = "text">24</span> hours</Card.Title>
                        <Card.Text>
                                <p className = "score score-green">{'+' + data24Hours.positive}</p>
                                <p className = "score-green">positive</p>
                                <p className = "score score-red">{'-' + data24Hours.negative}</p>
                                <p className = "score-red">negative</p>
                                <p>Out of <span className = "text">{data24Hours.tweet_count}</span> tweets</p>
                        </Card.Text>
                    </Card.Body>
                </Card>
                <Card className = 'cardDesign'>
                    <Card.Body>
                        <Card.Title >Past <span className = "text">30</span> days</Card.Title>
                        <Card.Text>
                                <p className = "score score-green">{'+' + data30Days.positive}</p>
                                <p className = "score-green">positive</p>
                                <p className = "score score-red">{'-' + data30Days.negative}</p>
                                <p className = "score-red">negative</p>
                                <p>Out of <span className = "text">{data30Days.tweet_count}</span> tweets</p>
                        </Card.Text>
                    </Card.Body>
                </Card>
                
            </div>
            <p style={{marginTop: '1rem'}}>Data Last Updated at: {new Date().toLocaleString()}</p>
            <Button variant ="secondary" size = "lg" type = 'submit' onClick = {formSubmit} style ={{width: '20%'}}>Refresh</Button>

        </React.Fragment>
        

    )
}

export default AggregatedSentiments;
