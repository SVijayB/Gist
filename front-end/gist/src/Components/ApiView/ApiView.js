import React, { useEffect, useState } from 'react';
import axios from "axios";
import './ApiView.css'
import FileIcon from '../../Images/file_upload_icon.svg'
import ArticleIcon from '../../Images/article.svg'
import Upload from './Upload';

const BaseUrl="http://127.0.0.1:5000/api/summarize?"


function ApiView(props){
   const [post, setPost] = useState(null); //returns a array
   const [Url,SetUrl]=useState('');
   const [File,SetFile]=useState('');
   const [Text,setText]=useState('UPLOAD OR ENTER URL')
   const [Opt,SetOpt]=useState("1")
   const [UserHist,SetUserHist]=useState([])





  function SwitchHandler(event){
    const userinpt=event.target.getAttribute("data-value");
    SetOpt(userinpt);
    if(Text==='ENTER URL')
    setText("Choose document you want to Upload");
    else
     setText("ENTER URL");
  }

  const OnSubmitHandler=(event)=>{
    event.preventDefault();
    if(Opt==='1'){
       const FileObj={
      name:'WEB',
     }
     SetUserHist([FileObj,...UserHist])
    }else{
     //file
     const FileObj={
      name:File.name,
      size:File.size,
      type:File.type
     }
     SetUserHist([FileObj,...UserHist])
     
    }
  }

  const OnChangeHandler=(event)=>{
     if(event.target.id==='Url')
      SetUrl(event.target.value);
     else
      SetFile(event.target.files[0])
   
  }
  
  useEffect(()=>{
    console.log(UserHist)
  },[UserHist])
 /* useEffect(()=>{
    console.log(Url)
  },[Url])
    useEffect(()=>{
    console.log("file"+File)
  },[File]) */

  return(
  
    <>
    <div className='Api_container'>
        
        <div className='upload_container'>
            
            <div className='upload_header'>
                <h1>UPLOAD OR ENTER URL</h1>
                <div >
                   <img src={FileIcon} alt="File Icon"  data-value="1" onClick={SwitchHandler}/>
                   <img src={ArticleIcon} alt="Article Icon" data-value="2"onClick={SwitchHandler}/>
                </div>
            </div>
            <div className='upload_playload'>

               <Upload  option={Opt} formsubmission={OnSubmitHandler} url={OnChangeHandler} text={Text} data={UserHist}/> 
               
            </div>


        </div>

    </div>
    </>

  );

}



export default ApiView;

/*
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
*/