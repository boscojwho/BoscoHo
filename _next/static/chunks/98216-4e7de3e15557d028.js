(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[98216],{56953:function(e,t,r){"use strict";r.d(t,{Z:function(){return a}});var n=r(45711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let a=(0,n.Z)("Mail",[["rect",{width:"20",height:"16",x:"2",y:"4",rx:"2",key:"18n3k1"}],["path",{d:"m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7",key:"1ocrg3"}]])},77232:function(e,t,r){"use strict";r.d(t,{Z:function(){return a}});var n=r(45711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let a=(0,n.Z)("Menu",[["line",{x1:"4",x2:"20",y1:"12",y2:"12",key:"1e0a9i"}],["line",{x1:"4",x2:"20",y1:"6",y2:"6",key:"1owob3"}],["line",{x1:"4",x2:"20",y1:"18",y2:"18",key:"yk5zj1"}]])},7572:function(e,t,r){"use strict";r.d(t,{Z:function(){return a}});var n=r(45711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let a=(0,n.Z)("MessageCircleHeart",[["path",{d:"M7.9 20A9 9 0 1 0 4 16.1L2 22Z",key:"vv11sd"}],["path",{d:"M15.8 9.2a2.5 2.5 0 0 0-3.5 0l-.3.4-.35-.3a2.42 2.42 0 1 0-3.2 3.6l3.6 3.5 3.6-3.5c1.2-1.2 1.1-2.7.2-3.7",key:"43lnbm"}]])},71665:function(e,t,r){"use strict";r.d(t,{Z:function(){return a}});var n=r(45711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let a=(0,n.Z)("Rss",[["path",{d:"M4 11a9 9 0 0 1 9 9",key:"pv89mb"}],["path",{d:"M4 4a16 16 0 0 1 16 16",key:"k0647b"}],["circle",{cx:"5",cy:"19",r:"1",key:"bfqh0e"}]])},97498:function(e,t){"use strict";var r,n;Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var r in t)Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}(t,{PrefetchKind:function(){return r},ACTION_REFRESH:function(){return a},ACTION_NAVIGATE:function(){return l},ACTION_RESTORE:function(){return o},ACTION_SERVER_PATCH:function(){return u},ACTION_PREFETCH:function(){return i},ACTION_FAST_REFRESH:function(){return c},ACTION_SERVER_ACTION:function(){return f}});let a="refresh",l="navigate",o="restore",u="server-patch",i="prefetch",c="fast-refresh",f="server-action";(n=r||(r={})).AUTO="auto",n.FULL="full",n.TEMPORARY="temporary",("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},10030:function(e,t,r){"use strict";function getDomainLocale(e,t,r,n){return!1}Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"getDomainLocale",{enumerable:!0,get:function(){return getDomainLocale}}),r(22866),("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},65170:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return b}});let n=r(38754),a=n._(r(67294)),l=r(74450),o=r(92227),u=r(64364),i=r(10109),c=r(73607),f=r(11823),s=r(89031),p=r(40920),d=r(10030),y=r(77192),v=r(97498),h=new Set;function prefetch(e,t,r,n,a,l){if(!l&&!(0,o.isLocalURL)(t))return;if(!n.bypassPrefetchedCheck){let a=void 0!==n.locale?n.locale:"locale"in e?e.locale:void 0,l=t+"%"+r+"%"+a;if(h.has(l))return;h.add(l)}let u=l?e.prefetch(t,a):e.prefetch(t,r,n);Promise.resolve(u).catch(e=>{})}function isModifiedEvent(e){let t=e.currentTarget,r=t.getAttribute("target");return r&&"_self"!==r||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.nativeEvent&&2===e.nativeEvent.which}function linkClicked(e,t,r,n,l,u,i,c,f,s){let{nodeName:p}=e.currentTarget,d="A"===p.toUpperCase();if(d&&(isModifiedEvent(e)||!f&&!(0,o.isLocalURL)(r)))return;e.preventDefault();let navigate=()=>{let e=null==i||i;"beforePopState"in t?t[l?"replace":"push"](r,n,{shallow:u,locale:c,scroll:e}):t[l?"replace":"push"](n||r,{forceOptimisticNavigation:!s,scroll:e})};f?a.default.startTransition(navigate):navigate()}function formatStringOrUrl(e){return"string"==typeof e?e:(0,u.formatUrl)(e)}let g=a.default.forwardRef(function(e,t){let r,n;let{href:o,as:u,children:h,prefetch:g=null,passHref:b,replace:m,shallow:_,scroll:k,locale:x,onClick:O,onMouseEnter:C,onTouchStart:M,legacyBehavior:E=!1,...j}=e;r=h,E&&("string"==typeof r||"number"==typeof r)&&(r=a.default.createElement("a",null,r));let w=a.default.useContext(f.RouterContext),P=a.default.useContext(s.AppRouterContext),R=null!=w?w:P,T=!w,A=!1!==g,I=null===g?v.PrefetchKind.AUTO:v.PrefetchKind.FULL,{href:L,as:N}=a.default.useMemo(()=>{if(!w){let e=formatStringOrUrl(o);return{href:e,as:u?formatStringOrUrl(u):e}}let[e,t]=(0,l.resolveHref)(w,o,!0);return{href:e,as:u?(0,l.resolveHref)(w,u):t||e}},[w,o,u]),S=a.default.useRef(L),U=a.default.useRef(N);E&&(n=a.default.Children.only(r));let Z=E?n&&"object"==typeof n&&n.ref:t,[K,D,H]=(0,p.useIntersection)({rootMargin:"200px"}),F=a.default.useCallback(e=>{(U.current!==N||S.current!==L)&&(H(),U.current=N,S.current=L),K(e),Z&&("function"==typeof Z?Z(e):"object"==typeof Z&&(Z.current=e))},[N,Z,L,H,K]);a.default.useEffect(()=>{R&&D&&A&&prefetch(R,L,N,{locale:x},{kind:I},T)},[N,L,D,x,A,null==w?void 0:w.locale,R,T,I]);let X={ref:F,onClick(e){E||"function"!=typeof O||O(e),E&&n.props&&"function"==typeof n.props.onClick&&n.props.onClick(e),R&&!e.defaultPrevented&&linkClicked(e,R,L,N,m,_,k,x,T,A)},onMouseEnter(e){E||"function"!=typeof C||C(e),E&&n.props&&"function"==typeof n.props.onMouseEnter&&n.props.onMouseEnter(e),R&&(A||!T)&&prefetch(R,L,N,{locale:x,priority:!0,bypassPrefetchedCheck:!0},{kind:I},T)},onTouchStart(e){E||"function"!=typeof M||M(e),E&&n.props&&"function"==typeof n.props.onTouchStart&&n.props.onTouchStart(e),R&&(A||!T)&&prefetch(R,L,N,{locale:x,priority:!0,bypassPrefetchedCheck:!0},{kind:I},T)}};if((0,i.isAbsoluteUrl)(N))X.href=N;else if(!E||b||"a"===n.type&&!("href"in n.props)){let e=void 0!==x?x:null==w?void 0:w.locale,t=(null==w?void 0:w.isLocaleDomain)&&(0,d.getDomainLocale)(N,e,null==w?void 0:w.locales,null==w?void 0:w.domainLocales);X.href=t||(0,y.addBasePath)((0,c.addLocale)(N,e,null==w?void 0:w.defaultLocale))}return E?a.default.cloneElement(n,X):a.default.createElement("a",{...j,...X},r)}),b=g;("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},40920:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"useIntersection",{enumerable:!0,get:function(){return useIntersection}});let n=r(67294),a=r(63436),l="function"==typeof IntersectionObserver,o=new Map,u=[];function createObserver(e){let t;let r={root:e.root||null,margin:e.rootMargin||""},n=u.find(e=>e.root===r.root&&e.margin===r.margin);if(n&&(t=o.get(n)))return t;let a=new Map,l=new IntersectionObserver(e=>{e.forEach(e=>{let t=a.get(e.target),r=e.isIntersecting||e.intersectionRatio>0;t&&r&&t(r)})},e);return t={id:r,observer:l,elements:a},u.push(r),o.set(r,t),t}function observe(e,t,r){let{id:n,observer:a,elements:l}=createObserver(r);return l.set(e,t),a.observe(e),function(){if(l.delete(e),a.unobserve(e),0===l.size){a.disconnect(),o.delete(n);let e=u.findIndex(e=>e.root===n.root&&e.margin===n.margin);e>-1&&u.splice(e,1)}}}function useIntersection(e){let{rootRef:t,rootMargin:r,disabled:o}=e,u=o||!l,[i,c]=(0,n.useState)(!1),f=(0,n.useRef)(null),s=(0,n.useCallback)(e=>{f.current=e},[]);(0,n.useEffect)(()=>{if(l){if(u||i)return;let e=f.current;if(e&&e.tagName){let n=observe(e,e=>e&&c(e),{root:null==t?void 0:t.current,rootMargin:r});return n}}else if(!i){let e=(0,a.requestIdleCallback)(()=>c(!0));return()=>(0,a.cancelIdleCallback)(e)}},[u,r,t,i,f.current]);let p=(0,n.useCallback)(()=>{c(!1)},[]);return[s,i,p]}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},41664:function(e,t,r){e.exports=r(65170)},33951:function(e,t,r){"use strict";r.d(t,{XQ:function(){return mapResponsive}});var n=r(25432);function mapResponsive(e,t){return Array.isArray(e)?e.map(e=>null===e?null:t(e)):(0,n.Kn)(e)?Object.keys(e).reduce((r,n)=>(r[n]=t(e[n]),r),{}):null!=e?t(e):null}Object.freeze(["base","sm","md","lg","xl","2xl"])},80552:function(e,t,r){"use strict";r.d(t,{E:function(){return f},U:function(){return s}});var n=r(35059),a=r(33179),l=r(51337),o=r(25432),u=r(33951),i=r(67294),c=r(85893);function px(e){return"number"==typeof e?`${e}px`:e}var f=(0,n.G)(function(e,t){let{spacing:r="0.5rem",spacingX:n,spacingY:f,children:p,justify:d,direction:y,align:v,className:h,shouldWrapChildren:g,...b}=e,m=(0,i.useMemo)(()=>{let{spacingX:e=r,spacingY:t=r}={spacingX:n,spacingY:f};return{"--chakra-wrap-x-spacing":t=>(0,u.XQ)(e,e=>px((0,a.fr)("space",e)(t))),"--chakra-wrap-y-spacing":e=>(0,u.XQ)(t,t=>px((0,a.fr)("space",t)(e))),"--wrap-x-spacing":"calc(var(--chakra-wrap-x-spacing) / 2)","--wrap-y-spacing":"calc(var(--chakra-wrap-y-spacing) / 2)",display:"flex",flexWrap:"wrap",justifyContent:d,alignItems:v,flexDirection:y,listStyleType:"none",padding:"0",margin:"calc(var(--wrap-y-spacing) * -1) calc(var(--wrap-x-spacing) * -1)","& > *:not(style)":{margin:"var(--wrap-y-spacing) var(--wrap-x-spacing)"}}},[r,n,f,d,v,y]),_=(0,i.useMemo)(()=>g?i.Children.map(p,(e,t)=>(0,c.jsx)(s,{children:e},t)):p,[p,g]);return(0,c.jsx)(l.m.div,{ref:t,className:(0,o.cx)("chakra-wrap",h),overflow:"hidden",...b,children:(0,c.jsx)(l.m.ul,{className:"chakra-wrap__list",__css:m,children:_})})});f.displayName="Wrap";var s=(0,n.G)(function(e,t){let{className:r,...n}=e;return(0,c.jsx)(l.m.li,{ref:t,__css:{display:"flex",alignItems:"flex-start"},className:(0,o.cx)("chakra-wrap__listitem",r),...n})});s.displayName="WrapItem"}}]);