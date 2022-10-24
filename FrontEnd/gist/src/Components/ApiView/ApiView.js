import React, { useState } from 'react';
import axios from "axios";
import './ApiView.css'



const BaseUrl="http://127.0.0.1:5000/api/summarize?"


function ApiView(props){
   const [post, setPost] = useState(null); //returns a array
   const [Url,SetUrl]=useState('');
   const [Title,SetTitle]=useState(null)
   const [Summary,Setsummary]=useState(null);
   const [File,SetFile]=useState('');

   function OnChangeHandler(event){
        SetUrl(event.target.value);
        console.log("VALUE : "+event.target.value);
   }
   
   function OnChangeHandlerFile(event){
        SetFile(event.target.files[0]);
        console.log(event.target.files[0]);
   }



   function OnSubmitHandler(event){
     axios.get(`${BaseUrl}type=1&link=${Url}`).then((res)=>{
      setPost(res.data.article);
      SetTitle(res.data.title);
      Setsummary(res.data.summary);
    });
   }

   function FileSubmitHandler(event){
     event.preventDefault();
     const formData = new FormData();
     formData.append("FILE",File);
     const config = {
      headers: {
        enctype: "multipart/form-data",
      },
    };
    axios.post(`http://127.0.0.1:5000/api/summarize/file`,formData,config).then((res)=>{
      console.log(res.data)
      setPost(res.data.article);
      SetTitle(res.data.title);
      Setsummary(res.data.summary);
    }).catch(e=>{
      console.log(e);
    });
   }
  
  return(
   <div className="api_container">
     
     <div className="SideBar_container">
         
        <div className="SideBar">
                <div className="api_content">
                      <div>ENTER/UPLOAD</div>
                      <div>
                            
                              < UserFormData type="text" text="URL" onchange={OnChangeHandler} value={Url}/>
                              <SubMitBtn handler={OnSubmitHandler}/>
                              <div> OR </div>
                              < UserFormData type="file" text="FILE" onchange={OnChangeHandlerFile} />
                              <SubMitBtn handler={FileSubmitHandler}/>
                              
                      </div>
                </div>
        </div>

      </div>
    
        <div>
           <div className="api_res">
              <div><h1>TITLE : {Title}</h1></div>
               <div><h3> Summary : {Summary} </h3></div>
               <p className=''>{post}</p>
           </div>
        </div>
        
    <div>
        
    </div>

   </div>
    

  );

}

function UserFormData(props){

  return(
    <> <div>
          <label  htmlFor={props.type}>{props.text}</label>
      </div>
        <input  value={props.value} id={props.type} name={props.type} type={props.type} onChange={props.onchange} />
    </>
  );
}

function SubMitBtn(props){
  return <><button type='submit' onClick={props.handler} >SUBMIT</button></>
}

export default ApiView;

// <button type="submit" onClick={OnSubmitHandler}>SUBMIT</button>