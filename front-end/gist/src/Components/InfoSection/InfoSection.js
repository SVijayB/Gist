import './InfoSection.css'
import Pic1 from '../../Images/vj1.jpg'
import Pic2 from '../../Images/naveen.jpg'
import Pic3 from '../../Images/santosh.jpg'


function InfoSection(props){

  const onClickHandler = (path) =>{
    window.open(path,'_blank')
  }
 
   return (
    <>
    <div className="AboutProjectSection" id="AboutSection">
        <div className="AbtText size1 center-text">
           About Project
        </div>
        <div className="AbtText size2 center-text">
            <p>
               Gist started out as a project built as part of NMIT Hacks 2021 and even came runners up! 
It was then further developed with improved models, an added front-end and features enhanced.
Gist started as a simple prototype to easily and efficiently summarize any news article into 60 or lesser words for quicker grasp of data, but since then it's come a long way. Today Gist hosts 3 seperate applications, each with their own unique functionalities, yet derived from the same core. 
Gist summarizes content from text, documents, pdfs, images so you can upload your physical news paper! And even other online news websites. This helps you consume important data much quicker.
Gist at it's heart as a core application acts as a medium where you can read several 60 or lesser word news articles in one place, similar to that of inShorts.
And finally the Gmail Summarizer was built to quickly get insights on your email data as it becomes harder everyday to keep track of the infinite mails we recieve everyday.
And thanks to the devs for making Gist open source, it can be easily accessed and updated by users from around the world and it's features only growing everyday!
            </p>
        </div>
    </div>

     
    <div className="infoseaction">
        <div className="Team" id="team">
              Meet Our Team
        </div>
        <div className="flex_list">
                <div className="User_Imgs">
                  <div className="DImg" onClick={()=> onClickHandler('https://github.com/SVijayB')} >
                    <img src={Pic1} alt="PIC" />
                  </div>
                </div>
                <div className="User_Imgs">
                  <div className="DImg" onClick={()=> onClickHandler('https://github.com/engineerscodes')}>
                    <img src={Pic2} alt="PIC" />
                  </div>
                </div>
                <div className="User_Imgs">
                  <div className="DImg" onClick={()=> onClickHandler('https://github.com/srisanthoshreddy-medapati')}>
                    <img src={Pic3} alt="PIC" />
                  </div>
                </div>
        </div>
    </div>
   </>);


}


export default InfoSection;