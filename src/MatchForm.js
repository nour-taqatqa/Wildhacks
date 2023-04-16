import React, { Component, useEffect, useState } from 'react'

function MatchForm () {

    const url =""
    const [data, setData] = useState({
        username: "",
        firstName: ""
    })

    function handle(e){
        const newdata = {...data}
        newdata[e.target.id] = e.target.value
        setData(newdata)
        console.log(newdata)
    }

    function submit(e){
        e.preventDefault()
        
        const data = new FormData(e.target)
        const value = Object.fromEntries(data.entries())

        console.log({value})
    }

    const form = document.querySelector('form')
    form.addEventListener('submit', submit)

    return (
        <div>
            <form onSubmit={(e)=> submit(e)}>
                <input 
                onChange={(e)=> handle(e)}
                id="username"
                value={data.username}
                placeholder="username" 
                type="text">
                </input>
                <input 
                onChange={(e)=> handle(e)}
                id="firstName"
                value={data.firstName}
                placeholder="firstName" 
                type="text"></input>

                <button>
                    Submit
                </button>
            </form>
        </div>
    )
}

export default MatchForm