import './InfoSection.css'
import Pic from '../../Images/pic.webp'

function InfoSection(props){
 
   return (
    <>
    <div className="AboutProjectSection" id="AboutSection">
        <div className="AbtText size1 center-text">
           About Project
        </div>
        <div className="AbtText size2">
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat nibh in nulla pretium consectetur.
                 Duis luctus tortor ut interdum feugiat. Class aptent taciti sociosqu ad litora torquent per conubia nostra,
                  per inceptos himenaeos. Suspendisse a velit eu risus dapibus ultrices non sit amet nisi. Quisque non sapien convallis, 
                  condimentum sem at, efficitur ipsum. Phasellus placerat varius elementum. Morbi porta non augue et tincidunt. 
                  Mauris cursus turpis bibendum leo tincidunt, at ultricies justo pharetra. Fusce ac metus iaculis, finibus nisi et, ultrices dui. 
                Aenean semper elit vel leo feugiat elementum. Praesent accumsan augue at erat iaculis vestibulum. Pellentesque turpis nibh.
            </p>
        </div>
    </div>

     
    <div className="infoseaction">
        <div className="Team" id="team">
              Meet Our Team
        </div>
        <div className="flex_list">
                <div className="User_Imgs">
                  <div className="DImg">
                    <img src={Pic} alt="PIC" />
                  </div>
                </div>
                <div className="User_Imgs">
                  <div className="DImg">
                    <img src={Pic} alt="PIC" />
                  </div>
                </div>
                <div className="User_Imgs">
                  <div className="DImg">
                    <img src={Pic} alt="PIC" />
                  </div>
                </div>
        </div>
    </div>
   </>);


}


export default InfoSection;