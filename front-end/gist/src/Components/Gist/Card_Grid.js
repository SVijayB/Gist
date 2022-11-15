import Card from './Card';
import './card.css'
import React, {  useState,useEffect } from 'react';
import axios from "axios";
import GridModal from '../Modal/GistModal'
const BaseUrl="http://127.0.0.1:5000/api/gist/app"

function CardGrid(props){

   const [modaldata,setmodaldata] = useState("")
   const [openModal,setModal] = useState(false)
   const [cards,setcards] = useState([])

   let page =0;

    const app =()=>{
      axios.get(`${BaseUrl}?page=${page}`).then((res)=>{
         
         if(parseInt(res.data.length)>0){
            
         setcards((prevstate)=>{
            const array =[...prevstate]
            for(let i=0;i<res.data.length;i++){
            array.push(res.data[i])
            }
         return array
         })
           page=page+1
         }
    });
    }

    const ModalState =(event)=>{
        window.removeEventListener('scroll',handleScroll)
        setModal(!openModal)
        let index = event.target.getAttribute("data-position")
        let data = cards[index];
        setmodaldata(data)
    }

     
    useEffect(()=>{
      window.addEventListener('scroll',handleScroll)
      app()
    }, []) // eslint-disable-line react-hooks/exhaustive-deps
   
    const handleScroll=(event)=>{
     
       if(event.target.localName ===undefined ){
            const { scrollTop, clientHeight, scrollHeight } = document.documentElement;
            
            if (scrollTop + clientHeight >=scrollHeight ) {
                app()
            }
       }
   
    }

   const closeModal =()=>{
    setModal(!openModal)
  }



return(<>
   <div className="grid">
 { !openModal?
         cards.map((data,index)=>(
            
             <Card  key={index} dt={data.dateAndTime} img={data.image}
             summary={data.summary} t={data.title} more={data.url}  fn={ModalState} pos={index}/>
         ))
         :null
      }
   </div>
   <GridModal open={openModal}  closebtn={closeModal} img={modaldata.image}
    title={modaldata.title} summary={modaldata.summary} dt={modaldata.dateAndTime} more={modaldata.url}
    
    />
   </>
);

}


export default CardGrid;