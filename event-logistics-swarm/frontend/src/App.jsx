import { useState } from "react"
import axios from "axios"

function App(){

const [eventName,setEventName]=useState("")
const [audience,setAudience]=useState("")
const [platform,setPlatform]=useState("")
const [eventDetails,setEventDetails]=useState("")

const [result,setResult]=useState(null)
const [logs,setLogs]=useState([])
const [status,setStatus]=useState("IDLE")

const [activeAgent,setActiveAgent]=useState(null)

const [updatedSchedule,setUpdatedSchedule]=useState([])
const [notifications,setNotifications]=useState([])



/* RUN SWARM */

const runSwarm = async () => {

try{

setStatus("RUNNING")
setLogs([])

setActiveAgent("content")
setLogs(prev=>[...prev,"Content agent generating campaign"])

setTimeout(()=>{

setActiveAgent("analytics")
setLogs(prev=>[...prev,"Analytics agent evaluating engagement"])

},1500)

setTimeout(()=>{

setActiveAgent("scheduler")
setLogs(prev=>[...prev,"Scheduler agent building event timeline"])

},3000)

setTimeout(()=>{

setActiveAgent("email")
setLogs(prev=>[...prev,"Email agent preparing participant emails"])

},4500)

const response = await axios.post(
"http://127.0.0.1:8000/run-swarm",
{
event_name:eventName,
audience:audience,
platform:platform,
event_details:eventDetails
}
)

setResult(response.data)
setLogs(prev=>[...prev,"Swarm execution completed"])
setActiveAgent(null)

setStatus("COMPLETED")

}
catch(error){

console.error(error)
setStatus("ERROR")

}

}



/* DISRUPTION */

const simulateDisruption = async () => {

try{

const response = await axios.post(
"http://127.0.0.1:8000/simulate-disruption",
{
constraint_text:"Keynote speaker cancelled. Move keynote session later."
}
)

setUpdatedSchedule(response.data.updated_schedule)
setNotifications(response.data.notifications)

}
catch(error){

console.error(error)

}

}



/* APPROVAL */

const approveCampaign=()=>{
alert("Campaign approved and ready for publishing")
}

const approveSchedule=()=>{
alert("Schedule approved")
}

const sendEmails=()=>{
alert("Email distribution triggered")
}



return(

<div className="min-h-screen bg-gray-100 p-6">


{/* HEADER */}

<div className="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-500 text-white p-6 rounded-xl shadow mb-6">

<h1 className="text-4xl font-bold text-center">
AI Swarm Event Logistics Command Center
</h1>

<p className="text-center mt-2">
Autonomous Multi-Agent Event Management Platform
</p>

</div>



{/* SYSTEM STATUS */}

<div className="grid grid-cols-4 gap-4 mb-6">

<div className="bg-white p-4 rounded-xl shadow text-center">
<h3 className="text-sm text-gray-500">Swarm Status</h3>
<p className="font-bold">{status}</p>
</div>

<div className="bg-white p-4 rounded-xl shadow text-center">
<h3 className="text-sm text-gray-500">Agents Online</h3>
<p className="font-bold">4</p>
</div>

<div className="bg-white p-4 rounded-xl shadow text-center">
<h3 className="text-sm text-gray-500">Tasks Completed</h3>
<p className="font-bold">{logs.length}</p>
</div>

<div className="bg-white p-4 rounded-xl shadow text-center">
<h3 className="text-sm text-gray-500">Emails Prepared</h3>
<p className="font-bold">{result?.emails?.length || 0}</p>
</div>

</div>



{/* SWARM PIPELINE */}

<div className="bg-white p-6 rounded-xl shadow mb-6">

<h2 className="text-xl font-semibold mb-4">
Swarm Execution Pipeline
</h2>

<div className="flex justify-between text-center">

<div className={`p-4 rounded-lg ${activeAgent==="content"?"bg-blue-500 text-white":"bg-gray-200"}`}>
📢 Content Agent
</div>

<div className="text-2xl">→</div>

<div className={`p-4 rounded-lg ${activeAgent==="analytics"?"bg-purple-500 text-white":"bg-gray-200"}`}>
📊 Analytics Agent
</div>

<div className="text-2xl">→</div>

<div className={`p-4 rounded-lg ${activeAgent==="scheduler"?"bg-green-500 text-white":"bg-gray-200"}`}>
📅 Scheduler Agent
</div>

<div className="text-2xl">→</div>

<div className={`p-4 rounded-lg ${activeAgent==="email"?"bg-pink-500 text-white":"bg-gray-200"}`}>
✉ Email Agent
</div>

</div>

</div>



<div className="grid grid-cols-3 gap-6">


{/* CONTROL PANEL */}

<div className="bg-white p-6 rounded-xl shadow">

<h2 className="text-xl font-semibold mb-4">
Event Control Panel
</h2>

<input
className="border p-2 w-full mb-3 rounded"
placeholder="Event Name"
onChange={(e)=>setEventName(e.target.value)}
/>

<input
className="border p-2 w-full mb-3 rounded"
placeholder="Target Audience"
onChange={(e)=>setAudience(e.target.value)}
/>

<input
className="border p-2 w-full mb-3 rounded"
placeholder="Marketing Platform"
onChange={(e)=>setPlatform(e.target.value)}
/>

<textarea
className="border p-2 w-full mb-3 rounded"
rows="4"
placeholder="Event Constraints / Details"
onChange={(e)=>setEventDetails(e.target.value)}
/>

<button
onClick={runSwarm}
className="bg-blue-600 text-white px-4 py-2 rounded mr-3">
Run AI Swarm
</button>

<button
onClick={simulateDisruption}
className="bg-red-500 text-white px-4 py-2 rounded">
Simulate Disruption
</button>

</div>



{/* TERMINAL EXECUTION LOG */}

<div className="bg-gray-900 text-green-400 p-6 rounded-xl shadow font-mono">

<h2 className="text-white mb-4">
Swarm Execution Logs
</h2>

{logs.map((log,i)=>(
<div key={i}>
{">"} {log}
</div>
))}

</div>



{/* AGENT STATUS */}

<div className="bg-white p-6 rounded-xl shadow">

<h2 className="text-xl font-semibold mb-4">
Agent Status
</h2>

<p>Content Agent: READY</p>
<p>Analytics Agent: READY</p>
<p>Scheduler Agent: READY</p>
<p>Email Agent: READY</p>

</div>

</div>



{/* AI OUTPUTS */}

{result &&(

<div className="grid grid-cols-3 gap-6 mt-6">


<div className="bg-white p-6 rounded-xl shadow">

<h2 className="text-xl font-semibold mb-3">
AI Marketing Campaign
</h2>

<pre className="text-sm whitespace-pre-wrap">
{result.campaign}
</pre>

<button
onClick={approveCampaign}
className="bg-green-500 text-white px-3 py-1 mt-3 rounded">
Approve Campaign
</button>

</div>



<div className="bg-white p-6 rounded-xl shadow">

<h2 className="text-xl font-semibold mb-3">
AI Event Timeline
</h2>

{result.schedule.map((s,i)=>(
<div key={i}>
{s.start} — {s.event}
</div>
))}

<button
onClick={approveSchedule}
className="bg-green-500 text-white px-3 py-1 mt-3 rounded">
Approve Schedule
</button>

</div>



<div className="bg-white p-6 rounded-xl shadow">

<h2 className="text-xl font-semibold mb-3">
Email Queue
</h2>

{result.emails.map((e,i)=>(
<div key={i}>
<b>{e.email}</b>
<p className="text-sm">{e.message}</p>
</div>
))}

<button
onClick={sendEmails}
className="bg-blue-600 text-white px-3 py-1 mt-3 rounded">
Send Emails
</button>

</div>


</div>

)}



{/* DISRUPTION RESULT */}

{updatedSchedule.length>0 &&(

<div className="bg-white p-6 rounded-xl shadow mt-6">

<h2 className="text-xl font-semibold text-red-600 mb-3">
Updated Schedule After Disruption
</h2>

{updatedSchedule.map((s,i)=>(
<div key={i}>
{s.start} — {s.event}
</div>
))}

</div>

)}



{/* NOTIFICATIONS */}

{notifications.length>0 &&(

<div className="bg-white p-6 rounded-xl shadow mt-6">

<h2 className="text-xl font-semibold mb-3">
Participant Notifications
</h2>

{notifications.map((n,i)=>(
<div key={i}>
<b>{n.email}</b>
<p>{n.message}</p>
</div>
))}

</div>

)}



</div>

)

}

export default App