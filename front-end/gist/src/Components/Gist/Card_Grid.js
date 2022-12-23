import Card from './Card';
import './card.css'
import React, {  useState,useEffect,useRef,useCallback} from 'react';
import axios from "axios";
import Footer from '../Footer/Footer'
import GridModal from '../Modal/GistModal'
const BaseUrl="http://127.0.0.1:5000/api/gist/data"

function CardGrid(props){

   const [modaldata,setmodaldata] = useState("")
   const [openModal,setModal] = useState(false)
   const [TragetId,SetTragetId] = useState(0)
   const [cards,setcards] = useState([])
   const [page,setpage] = useState(1)
   const [HasMore,SetHasMore] = useState(true)
   const observer = useRef()
   const LastNewsCard = useCallback(node => {
      if(observer.current) observer.current.disconnect()
      observer.current = new IntersectionObserver(entries =>{
            if(entries[0].isIntersecting && HasMore){
               console.log("api call")
               app(page)
               setpage((prev)=> prev+1)
               
            }
      })
      if(node) observer.current.observe(node)
   },[cards,HasMore]) 

    const app =(PageNo)=>{
      axios.get(`${BaseUrl}?page=${PageNo}`).then((res)=>{
         if(res.data.length === 0)
           SetHasMore(false)

         if(parseInt(res.data.length)>0){
            
         setcards((prevstate)=>{
            const array =[...prevstate]
            for(let i=0;i<res.data.length;i++){
            array.push(res.data[i])
            }
         return array
         })
         }
    });
    }

    const ModalState =(event)=>{
        setModal(!openModal)
        let index = event.target.getAttribute("data-position")
        let data = cards[index];
        SetTragetId(index)
        setmodaldata(data)
    }
    
    useEffect(() => {
    const element = document.getElementById(TragetId)
    if (element && !openModal){
        element.scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"})
    }
    }, [TragetId,openModal])
     
    useEffect(()=>{
      app(0)
    }, []) // eslint-disable-line react-hooks/exhaustive-deps
   
   const closeModal =()=>{
      setModal(!openModal)
  }



return(<>
   <div className="grid">
 { !openModal?
         cards.map((data,index)=>{
              if (index+1 === cards.length)
               return  <Card  key={index} dt={data.dateAndTime} img={data.image} Innerref={LastNewsCard}
               summary={data.summary} t={data.title} more={data.url}  fn={ModalState} pos={index}/>
               else
               return  <Card  key={index} dt={data.dateAndTime} img={data.image} 
               summary={data.summary} t={data.title} more={data.url}  fn={ModalState} pos={index}/>

          })
         :null
  
      }
   </div>
   {!openModal?<Footer/>:null}
   <GridModal open={openModal}  closebtn={closeModal} img={modaldata.image}
    title={modaldata.title} summary={modaldata.summary} dt={modaldata.dateAndTime} more={modaldata.url}  
    />
   </>
);

}


export default CardGrid;