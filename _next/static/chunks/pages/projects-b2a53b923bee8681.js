(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[33327],{9182:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/projects",function(){return n(19444)}])},19444:function(e,t,n){"use strict";n.r(t),n.d(t,{Box_baa1d6bdb1b42aa44d0873c861717703:function(){return Box_baa1d6bdb1b42aa44d0873c861717703},Div_ac2a89ea84667d600a059f034bd91dfe:function(){return Div_ac2a89ea84667d600a059f034bd91dfe},Flex_7805bd6ebfc5bdff0adda9e0e333d5db:function(){return Flex_7805bd6ebfc5bdff0adda9e0e333d5db},Fragment_cf53a535ae2e610a113dd361eb6ac95b:function(){return Fragment_cf53a535ae2e610a113dd361eb6ac95b},Link_1ad693affe73cd5b5aa9af40944b87fa:function(){return Link_1ad693affe73cd5b5aa9af40944b87fa},Link_5ac732c2b8a7fdb9a416bad47ee3d74e:function(){return Link_5ac732c2b8a7fdb9a416bad47ee3d74e},Link_97cc29338fe21db30e3cf14259de1cec:function(){return Link_97cc29338fe21db30e3cf14259de1cec},Link_a355d8fb4eb426616e68a88d878a611c:function(){return Link_a355d8fb4eb426616e68a88d878a611c},Link_aa0746c549f582d6a3f312ab39c3ee66:function(){return Link_aa0746c549f582d6a3f312ab39c3ee66},Popover__content_93ed6ccf7e2e59654689efef9b8e7574:function(){return Popover__content_93ed6ccf7e2e59654689efef9b8e7574},Toaster_6e90e5e87a1cac8c96c683214079bef3:function(){return Toaster_6e90e5e87a1cac8c96c683214079bef3},default:function(){return Component}});var i=n(82729),a=n(35944),r=n(67294),c=n(60687),o=n(6608),d=n(77232),l=n(56953),s=n(7572),h=n(71665),m=n(15637),f=n(70917),u=n(64712),g=n(73954),p=n(58531),x=n(41664),b=n.n(x),w=n(80552),Z=n(35059),v=n(51337),_=n(85893),k=(0,Z.G)(function(e,t){let{templateAreas:n,gap:i,rowGap:a,columnGap:r,column:c,row:o,autoFlow:d,autoRows:l,templateRows:s,autoColumns:h,templateColumns:m,...f}=e;return(0,_.jsx)(v.m.div,{ref:t,__css:{display:"grid",gridTemplateAreas:n,gridGap:i,gridRowGap:a,gridColumnGap:r,gridAutoColumns:h,gridColumn:c,gridRow:o,gridAutoFlow:d,gridAutoRows:l,gridTemplateRows:s,gridTemplateColumns:m},...f})});k.displayName="Grid";var C=n(75119),S=n(34629),y=n(33951),F=(0,Z.G)(function(e,t){let{columns:n,spacingX:i,spacingY:a,spacing:r,minChildWidth:c,...o}=e,d=(0,C.F)(),l=c?widthToColumns(c,d):countToColumns(n);return(0,_.jsx)(k,{ref:t,gap:r,columnGap:i,rowGap:a,templateColumns:l,...o})});function toPx(e){return"number"==typeof e?`${e}px`:e}function widthToColumns(e,t){return(0,y.XQ)(e,e=>{let n=(0,S.LP)("sizes",e,toPx(e))(t);return null===e?null:`repeat(auto-fit, minmax(${n}, 1fr))`})}function countToColumns(e){return(0,y.XQ)(e,e=>null===e?null:`repeat(${e}, minmax(0, 1fr))`)}F.displayName="SimpleGrid";var G=(0,Z.G)(function(e,t){let{htmlWidth:n,htmlHeight:i,alt:a,...r}=e;return(0,_.jsx)("img",{width:n,height:i,ref:t,alt:a,...r})});G.displayName="NativeImage";var B=n(26245);function useImage(e){let{loading:t,src:n,srcSet:i,onLoad:a,onError:c,crossOrigin:o,sizes:d,ignoreFallback:l}=e,[s,h]=(0,r.useState)("pending");(0,r.useEffect)(()=>{h(n?"loading":"pending")},[n]);let m=(0,r.useRef)(),f=(0,r.useCallback)(()=>{if(!n)return;flush();let e=new Image;e.src=n,o&&(e.crossOrigin=o),i&&(e.srcset=i),d&&(e.sizes=d),t&&(e.loading=t),e.onload=e=>{flush(),h("loaded"),null==a||a(e)},e.onerror=e=>{flush(),h("failed"),null==c||c(e)},m.current=e},[n,o,i,d,a,c,t]),flush=()=>{m.current&&(m.current.onload=null,m.current.onerror=null,m.current=null)};return(0,B.G)(()=>{if(!l)return"loading"===s&&f(),()=>{flush()}},[s,f,l]),l?"loaded":s}var shouldShowFallbackImage=(e,t)=>"loaded"!==e&&"beforeLoadOrError"===t||"failed"===e&&"onError"===t;function omit(e,t=[]){let n=Object.assign({},e);for(let e of t)e in n&&delete n[e];return n}var H=(0,Z.G)(function(e,t){let{fallbackSrc:n,fallback:i,src:a,srcSet:r,align:c,fit:o,loading:d,ignoreFallback:l,crossOrigin:s,fallbackStrategy:h="beforeLoadOrError",referrerPolicy:m,...f}=e,u=null!=d||l||!(void 0!==n||void 0!==i),g=useImage({...e,crossOrigin:s,ignoreFallback:u}),p=shouldShowFallbackImage(g,h),x={ref:t,objectFit:o,objectPosition:c,...u?f:omit(f,["onError","onLoad"])};return p?i||(0,_.jsx)(v.m.img,{as:G,className:"chakra-image__placeholder",src:n,...x}):(0,_.jsx)(v.m.img,{as:G,src:a,srcSet:r,crossOrigin:s,loading:d,referrerPolicy:m,className:"chakra-image",...x})});H.displayName="Image";var T=n(9008),L=n.n(T);function _templateObject(){let e=(0,i._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}function Box_baa1d6bdb1b42aa44d0873c861717703(){let{resolvedColorMode:e}=(0,r.useContext)(c.kc);return(0,a.tZ)(p.xu,{css:{backgroundColor:(0,o.oA)("light"===e)?"rgba(250, 249, 246, 1)":"rgba(13, 13, 13, 0.8)",backdropFilter:"blur(4px)",width:"100%","@media screen and (min-width: 0)":{height:"80px",display:"flex"},"@media screen and (min-width: 30em)":{height:"80px",display:"flex"},"@media screen and (min-width: 48em)":{height:"80px",display:"flex"},"@media screen and (min-width: 62em)":{height:"0px",display:"none"},"@media screen and (min-width: 80em)":{height:"0px",display:"none"},"@media screen and (min-width: 96em)":{height:"0px",display:"none"},zIndex:"5",top:"0px",position:"fixed",alignItems:"center",direction:"column"},children:(0,a.BX)(p.kC,{align:"center",css:{width:"100%",marginLeft:"20px",marginRight:"20px",marginBottom:"20px"},children:[(0,a.tZ)(Link_aa0746c549f582d6a3f312ab39c3ee66,{}),(0,a.tZ)(p.kC,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,a.BX)(p.J2.fC,{modal:!0,children:[(0,a.tZ)(p.J2.xz,{children:(0,a.tZ)(p.zx,{children:(0,a.tZ)(d.Z,{css:{color:"var(--current-color)"}})})}),(0,a.tZ)(Popover__content_93ed6ccf7e2e59654689efef9b8e7574,{})]})]})})}function Link_5ac732c2b8a7fdb9a416bad47ee3d74e(){let e=(0,r.useContext)(c.M4.state);return(0,a.tZ)(p.rU,{asChild:!0,css:{"@media screen and (min-width: 0)":{width:"0%"},"@media screen and (min-width: 30em)":{width:"0%"},"@media screen and (min-width: 48em)":{width:"0%"},"@media screen and (min-width: 62em)":{width:"34%"},"@media screen and (min-width: 80em)":{width:"24%"},"@media screen and (min-width: 96em)":{width:"24%"},marginTop:"4px",marginBottom:"-6px","&:hover":{color:"var(--accent-8)"}},underline:"none",children:(0,a.tZ)(b(),{href:"/coding",passHref:!0,children:(0,a.tZ)(p.kC,{align:"center",className:"rx-Stack",css:{color:(0,o.oA)("/coding"===e.router.page.path||"Home"===("/"===e.router.page.path&&"Coding"))?"var(--ruby-10)":"var(--white-11)",width:"100%"},direction:"row",gap:"3",children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"600",fontSize:"2em",fontVariationSettings:"'slnt' 0",borderRadius:"4px",lineHeight:"0.8","&:hover":{color:"red"}},children:"CODING"})})})})}function Div_ac2a89ea84667d600a059f034bd91dfe(){let[e,t]=(0,r.useContext)(c.DR);return(0,a.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: ".concat(t.length>0?t[t.length-1].message:""),children:(0,a.tZ)(Fragment_cf53a535ae2e610a113dd361eb6ac95b,{})})}function Link_97cc29338fe21db30e3cf14259de1cec(){let e=(0,r.useContext)(c.M4.state);return(0,a.tZ)(p.rU,{asChild:!0,css:{"@media screen and (min-width: 0)":{width:"0%"},"@media screen and (min-width: 30em)":{width:"0%"},"@media screen and (min-width: 48em)":{width:"0%"},"@media screen and (min-width: 62em)":{width:"34%"},"@media screen and (min-width: 80em)":{width:"24%"},"@media screen and (min-width: 96em)":{width:"24%"},marginTop:"4px",marginBottom:"-6px","&:hover":{color:"var(--accent-8)"}},underline:"none",children:(0,a.tZ)(b(),{href:"/about",passHref:!0,children:(0,a.tZ)(p.kC,{align:"center",className:"rx-Stack",css:{color:(0,o.oA)("/about"===e.router.page.path||"Home"===("/"===e.router.page.path&&"About"))?"var(--ruby-10)":"var(--white-11)",width:"100%"},direction:"row",gap:"3",children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"600",fontSize:"2em",fontVariationSettings:"'slnt' 0",borderRadius:"4px",lineHeight:"0.8","&:hover":{color:"red"}},children:"ABOUT"})})})})}function Link_1ad693affe73cd5b5aa9af40944b87fa(){let e=(0,r.useContext)(c.M4.state);return(0,a.tZ)(p.rU,{asChild:!0,css:{"@media screen and (min-width: 0)":{width:"0%"},"@media screen and (min-width: 30em)":{width:"0%"},"@media screen and (min-width: 48em)":{width:"0%"},"@media screen and (min-width: 62em)":{width:"34%"},"@media screen and (min-width: 80em)":{width:"24%"},"@media screen and (min-width: 96em)":{width:"24%"},marginTop:"4px",marginBottom:"-6px","&:hover":{color:"var(--accent-8)"}},underline:"none",children:(0,a.tZ)(b(),{href:"/projects",passHref:!0,children:(0,a.tZ)(p.kC,{align:"center",className:"rx-Stack",css:{color:(0,o.oA)("/projects"===e.router.page.path||"Home"===("/"===e.router.page.path&&"Projects"))?"var(--ruby-10)":"var(--white-11)",width:"100%"},direction:"row",gap:"3",children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"600",fontSize:"2em",fontVariationSettings:"'slnt' 0",borderRadius:"4px",lineHeight:"0.8","&:hover":{color:"red"}},children:"PROJECTS"})})})})}let z=(0,f.F4)(_templateObject());function Link_aa0746c549f582d6a3f312ab39c3ee66(){let e=(0,r.useContext)(c.M4.state);return(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},underline:"none",children:(0,a.tZ)(b(),{href:"/",passHref:!0,children:(0,a.BX)(p.kC,{align:"start",className:"rx-Stack",css:{marginTop:"24px",color:(0,o.oA)("/"===e.router.page.path||"/"===e.router.page.path)?"var(--ruby-10)":"var(--white-11)"},direction:"column",gap:"0",children:[(0,a.tZ)(p.xv,{as:"p",css:{textAlign:"right",fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"800",fontSize:"36px",fontVariationSettings:"'slnt' 0",letterSpacing:"-2px",color:"var(--accent-10)",lineHeight:"0.8",width:"100%","&:hover":{color:"red"}},children:"bOSCO"}),(0,a.tZ)(p.xv,{as:"p",css:{textAlign:"right",fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"800",fontSize:"36px",fontVariationSettings:"'slnt' 0",letterSpacing:"-2px",color:"var(--accent-10)",lineHeight:"0.8",width:"100%","&:hover":{color:"red"}},children:"hO"})]})})})}function Flex_7805bd6ebfc5bdff0adda9e0e333d5db(){let{resolvedColorMode:e}=(0,r.useContext)(c.kc);return(0,a.BX)(p.kC,{css:{backgroundColor:(0,o.oA)("light"===e)?"#FAF9F6":"#0D0D0D"},justify:"center",gap:"2",children:[(0,a.tZ)(Box_baa1d6bdb1b42aa44d0873c861717703,{}),(0,a.BX)(p.kC,{css:{marginLeft:"20px",marginRight:"20px",height:"100%",minHeight:"100vh",width:"100%"},gap:"4",children:[(0,a.tZ)(p.xu,{css:{"@media screen and (min-width: 0)":{marginTop:"80px",width:"0%",display:"none"},"@media screen and (min-width: 30em)":{marginTop:"80px",width:"0%",display:"none"},"@media screen and (min-width: 48em)":{marginTop:"80px",width:"0%",display:"none"},"@media screen and (min-width: 62em)":{marginTop:"0px",width:"34%",display:"flex"},"@media screen and (min-width: 80em)":{marginTop:"0px",width:"24%",display:"flex"},"@media screen and (min-width: 96em)":{marginTop:"0px",width:"24%",display:"flex"},height:"100%",flexShrink:0},children:(0,a.BX)(p.kC,{align:"start",className:"rx-Stack",css:{position:"fixed","@media screen and (min-width: 0)":{width:"0%"},"@media screen and (min-width: 30em)":{width:"0%"},"@media screen and (min-width: 48em)":{width:"0%"},"@media screen and (min-width: 62em)":{width:"34%"},"@media screen and (min-width: 80em)":{width:"24%"},"@media screen and (min-width: 96em)":{width:"24%"}},direction:"column",gap:"2",children:[(0,a.tZ)(Link_a355d8fb4eb426616e68a88d878a611c,{}),(0,a.tZ)(p.xu,{css:{height:"32px"}}),(0,a.tZ)(Link_5ac732c2b8a7fdb9a416bad47ee3d74e,{}),(0,a.BX)(w.E,{align:"center",spacingX:"0.85em",children:[(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"swift/apple"})}),(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"python"})}),(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"web"})}),(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"blog/rss"})})]}),(0,a.tZ)(Link_1ad693affe73cd5b5aa9af40944b87fa,{}),(0,a.BX)(w.E,{align:"center",spacingX:"0.85em",children:[(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"hk glyph"})}),(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"chinotto"})}),(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"castro"})}),(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"open source"})}),(0,a.tZ)(w.U,{children:(0,a.tZ)(p.xv,{as:"p",css:{fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"300",fontSize:"1.1em",fontVariationSettings:"'slnt' 0",lineHeight:"0.9"},children:"past projects"})})]}),(0,a.tZ)(Link_97cc29338fe21db30e3cf14259de1cec,{}),(0,a.BX)(p.kC,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,a.tZ)(p.kC,{children:(0,a.tZ)(l.Z,{css:{color:"var(--current-color)"},size:15})}),(0,a.tZ)(p.kC,{children:(0,a.tZ)(s.Z,{css:{color:"var(--current-color)"},size:15})}),(0,a.tZ)(p.kC,{children:(0,a.tZ)(h.Z,{css:{color:"var(--current-color)"},size:15})})]})]})}),(0,a.tZ)(p.xu,{css:{"@media screen and (min-width: 0)":{marginTop:"80px",marginBottom:"80px",width:"100%"},"@media screen and (min-width: 30em)":{marginTop:"80px",marginBottom:"80px",width:"100%"},"@media screen and (min-width: 48em)":{marginTop:"80px",marginBottom:"80px",width:"100%"},"@media screen and (min-width: 62em)":{marginTop:"20px",marginBottom:"80px",width:"66%"},"@media screen and (min-width: 80em)":{marginTop:"20px",marginBottom:"80px",width:"58%"},"@media screen and (min-width: 96em)":{marginTop:"20px",marginBottom:"80px",width:"58%"},height:"100%"},children:(0,a.BX)(p.kC,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.BX)(F,{columns:[2,3,4],spacing:"6",children:[(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,a.tZ)(b(),{href:"/",passHref:!0,children:(0,a.BX)(p.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.tZ)(H,{src:"/hkscs_icon.png",sx:{width:"120px",height:"auto",borderRadius:"26.844"}}),(0,a.tZ)(p.xv,{as:"p",weight:"bold",children:"HK Characters"})]})})}),(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,a.tZ)(b(),{href:"https://github.com/boscojwho/Chinotto",passHref:!0,children:(0,a.BX)(p.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.tZ)(H,{src:"/chinotto_placeholder_logo.png",sx:{width:"120px",height:"auto",borderRadius:"26.844"}}),(0,a.tZ)(p.xv,{as:"p",weight:"bold",children:"Chinotto"})]})})}),(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,a.tZ)(b(),{href:"/",passHref:!0,children:(0,a.BX)(p.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.tZ)(H,{src:"/castro_icon.png",sx:{width:"120px",height:"auto",borderRadius:"26.844"}}),(0,a.tZ)(p.xv,{as:"p",weight:"bold",children:"Castro"})]})})})]}),(0,a.tZ)(p.Z0,{size:"4"}),(0,a.BX)(p.kC,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.tZ)(p.xv,{as:"p",weight:"medium",children:"Open Source Contributor"}),(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,a.tZ)(b(),{href:"https://github.com/mlemgroup/mlem",passHref:!0,children:(0,a.BX)(p.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.tZ)(H,{src:"/mlem_logo.png",sx:{width:"60px",height:"auto",borderRadius:"13.422"}}),(0,a.tZ)(p.xv,{as:"p",weight:"bold",children:"Mlem"})]})})})]}),(0,a.tZ)(p.Z0,{size:"4"}),(0,a.tZ)(p.xv,{as:"p",weight:"medium",children:"Fencing"}),(0,a.BX)(F,{columns:[4],spacing:"4",children:[(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,a.tZ)(b(),{href:"/",passHref:!0,children:(0,a.tZ)(p.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:(0,a.tZ)(H,{src:"/fencathon_2_logo.png",sx:{width:"44px",height:"auto",borderRadius:"9.8428"}})})})}),(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,a.tZ)(b(),{href:"/",passHref:!0,children:(0,a.tZ)(p.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:(0,a.tZ)(H,{src:"/fencathon_1_logo.png",sx:{width:"44px",height:"auto",borderRadius:"9.8428"}})})})}),(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,a.tZ)(b(),{href:"/",passHref:!0,children:(0,a.tZ)(p.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:(0,a.tZ)(H,{src:"/atp_logo.png",sx:{width:"44px",height:"auto",borderRadius:"9.8428"}})})})})]}),(0,a.tZ)(p.Z0,{size:"4"}),(0,a.tZ)(F,{columns:[4],spacing:"4",children:(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},children:(0,a.tZ)(b(),{href:"https://www.rungoapp.com/",passHref:!0,children:(0,a.BX)(p.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.tZ)(H,{src:"/rungo_icon_old.png",sx:{width:"44px",height:"auto",borderRadius:"9.8428"}}),(0,a.tZ)(H,{src:"/rungo_icon_new.png",sx:{width:"44px",height:"auto"}})]})})})})]})}),(0,a.tZ)(r.Fragment,{})]})]})}function Link_a355d8fb4eb426616e68a88d878a611c(){let e=(0,r.useContext)(c.M4.state);return(0,a.tZ)(p.rU,{asChild:!0,css:{"&:hover":{color:"var(--accent-8)"}},underline:"none",children:(0,a.tZ)(b(),{href:"/",passHref:!0,children:(0,a.BX)(p.kC,{align:"start",className:"rx-Stack",css:{marginTop:"24px",color:(0,o.oA)("/"===e.router.page.path||"/"===e.router.page.path)?"var(--ruby-10)":"var(--white-11)"},direction:"column",gap:"0",children:[(0,a.tZ)(p.xv,{as:"p",css:{textAlign:"right",fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"800",fontSize:"80px",fontVariationSettings:"'slnt' 0",letterSpacing:"-2px",color:"var(--accent-10)",lineHeight:"0.8",width:"100%","&:hover":{color:"red"}},children:"bOSCO"}),(0,a.tZ)(p.xv,{as:"p",css:{textAlign:"right",fontFamily:"Gluten","--default-font-family":"Gluten",fontWeight:"800",fontSize:"60px",fontVariationSettings:"'slnt' 0",letterSpacing:"-2px",color:"var(--accent-10)",lineHeight:"0.8",width:"100%","&:hover":{color:"red"}},children:"hO"})]})})})}function Fragment_cf53a535ae2e610a113dd361eb6ac95b(){let[e,t]=(0,r.useContext)(c.DR);return(0,a.tZ)(r.Fragment,{children:(0,o.oA)(t.length>0)?(0,a.tZ)(r.Fragment,{children:(0,a.tZ)(m.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:"".concat(z," 1s infinite")},size:32})}):(0,a.tZ)(r.Fragment,{})})}function Popover__content_93ed6ccf7e2e59654689efef9b8e7574(){let{resolvedColorMode:e}=(0,r.useContext)(c.kc);return(0,a.tZ)(p.J2.VY,{css:{background:(0,o.oA)("light"===e)?"#FEFCFB":"#1E160F"},children:(0,a.BX)(p.kC,{css:{width:"240px"},direction:"column",gap:"3",children:[(0,a.tZ)(Link_5ac732c2b8a7fdb9a416bad47ee3d74e,{}),(0,a.tZ)(Link_1ad693affe73cd5b5aa9af40944b87fa,{}),(0,a.tZ)(Link_97cc29338fe21db30e3cf14259de1cec,{}),(0,a.tZ)(p.J2.x8,{children:(0,a.tZ)(p.zx,{children:"Close"})})]})})}function Toaster_6e90e5e87a1cac8c96c683214079bef3(){let{resolvedColorMode:e}=(0,r.useContext)(c.kc);o.xL.__toast=u.A;let[t,n]=(0,r.useContext)(c.DR),i={description:"Check if server is reachable at ".concat((0,o.LH)(g.Ks).href),closeButton:!0,duration:12e4,id:"websocket-error"},[d,l]=(0,r.useState)(!1);return(0,r.useEffect)(()=>{n.length>=2?d||u.A.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...i,onDismiss:()=>l(!0)}):(u.A.dismiss("websocket-error"),l(!1))},[n]),(0,a.tZ)(u.x,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function Component(){return(0,a.BX)(r.Fragment,{children:[(0,a.BX)(r.Fragment,{children:[(0,a.tZ)(Div_ac2a89ea84667d600a059f034bd91dfe,{}),(0,a.tZ)(Toaster_6e90e5e87a1cac8c96c683214079bef3,{})]}),(0,a.tZ)(Flex_7805bd6ebfc5bdff0adda9e0e333d5db,{}),(0,a.BX)(L(),{children:[(0,a.tZ)("title",{children:"Projects"}),(0,a.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}}},function(e){e.O(0,[90477,98216,49774,92888,40179],function(){return e(e.s=9182)}),_N_E=e.O()}]);