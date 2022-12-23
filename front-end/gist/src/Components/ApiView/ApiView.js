import React, {  useEffect, useState } from 'react';
import axios from "axios";
import './ApiView.css'
import FileIcon from '../../Images/file_upload_icon.svg'
import ArticleIcon from '../../Images/article.svg'
import Upload from './Upload';

const BaseUrl="http://127.0.0.1:5000/api/summarize?"


function ApiView(props){
   const [Url,SetUrl]=useState('');
   const [File,SetFile]=useState('');
   const [Text,setText]=useState('UPLOAD OR ENTER URL')
   const [Opt,SetOpt]=useState("1")
   const [UserHist,SetUserHist]=useState([])

   const [UploadProg,SetUploadProg] = useState(0)
   


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
      SetUserHist((prev)=>{
      const FileObj={
        name:Url.replace(/(^\w+:|^)\/\//, '').split("/")[0],
        id:prev.length,
        bloburl:"#",
        UploadProg:98,
        Msg:"Processing"
      }
      PostArticle(FileObj.id)
      return [FileObj,...prev]
      })

    }
    else{
     const FileObj={
      name:File.name,
      size:File.size,
      type:File.type,
      id:UserHist.length,
      bloburl:"#",
      UploadProg:0,
      Msg:"Uploading"
     }
     FileSubmitHandler(FileObj.id)
     SetUserHist([FileObj,...UserHist])
     
    }
    console.log(UserHist)
  }

  function FileSubmitHandler(TargetIndex){
     const formData = new FormData();
     formData.append("FILE",File);
     const config = {
      headers: {
        enctype: "multipart/form-data",
      },
      responseType: 'blob',
      onUploadProgress: (progressEvent) => {
				const totalLength =  (progressEvent.loaded /progressEvent.total)*100
				console.log("onUploadProgress", totalLength);
        SetUserHist((prev)=>{
          let items =[...prev]
           items.find((item,i)=>{
            if(item.id===TargetIndex){
               items[i].UploadProg=totalLength
            }
            return true;
          })
          return items
       })
			}
    };
    axios.post(`http://127.0.0.1:5000/api/summarize/file?report=1`,formData,config,).then((res)=>{
       let blob = new Blob([res.data], {type: "application/pdf"});
       let fileURL = URL.createObjectURL(blob);
       window.open(fileURL,'_blank');
       //setbloburl([fileURL,...bloburl])
       SetUserHist((prev)=>{
          let items =[...prev]
           items.find((item,i)=>{
            if(item.id===TargetIndex){
               items[i].bloburl=fileURL
               items[i].Msg="Completed"
            }
            return true;
          })
          return items
       })
    }).catch(e=>{
      console.log(e);
    });
   }

  const PostArticle=(TargetIndex)=>{
    
    const config = {
      responseType: 'blob',
      onUploadProgress: (progressEvent) => {
				const totalLength =  (progressEvent.loaded /progressEvent.total)*100
				console.log("onUploadProgress", totalLength);
        SetUploadProg(totalLength)
			}
    };

     axios.get(`${BaseUrl}type=1&link=${Url}&report=1`,config).then((res)=>{
       let blob = new Blob([res.data], {type: "application/pdf"});
       let fileURL = URL.createObjectURL(blob);
       window.open(fileURL,'_blank');
        SetUserHist((prev)=>{
          let items =[...prev]
           items.find((item,i)=>{
            if(item.id===TargetIndex){
               items[i].bloburl=fileURL
               items[i].UploadProg=100
               items[i].Msg="Completed"
            }
            return true;
          })
          return items
       })
    });


  }
 
  const OnChangeHandler=(event)=>{
     if(event.target.id==='Url'){
      SetUrl(event.target.value);
     }
     else
      SetFile(event.target.files[0])
  }
  
  useEffect(()=>{
    console.log(UserHist)
  },[UserHist])

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

               <Upload  Up={UploadProg} option={Opt} formsubmission={OnSubmitHandler} 
                url={OnChangeHandler} text={Text} data={UserHist} /> 
               
            </div>


        </div>

    </div>
    </>

  );

}



export default ApiView;
