(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[234,63047,53444],{234:function(e,t,n){"use strict";var a=n(64836);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var r=a(n(61028)).default;t.default=r},93205:function(e){"use strict";function markupTemplating(e){!function(e){function getPlaceholder(e,t){return"___"+e.toUpperCase()+t+"___"}Object.defineProperties(e.languages["markup-templating"]={},{buildPlaceholders:{value:function(t,n,a,r){if(t.language===n){var o=t.tokenStack=[];t.code=t.code.replace(a,function(e){if("function"==typeof r&&!r(e))return e;for(var a,i=o.length;-1!==t.code.indexOf(a=getPlaceholder(n,i));)++i;return o[i]=e,a}),t.grammar=e.languages.markup}}},tokenizePlaceholders:{value:function(t,n){if(t.language===n&&t.tokenStack){t.grammar=e.languages[n];var a=0,r=Object.keys(t.tokenStack);walkTokens(t.tokens)}function walkTokens(o){for(var i=0;i<o.length&&!(a>=r.length);i++){var s=o[i];if("string"==typeof s||s.content&&"string"==typeof s.content){var l=r[a],u=t.tokenStack[l],g="string"==typeof s?s:s.content,p=getPlaceholder(n,l),c=g.indexOf(p);if(c>-1){++a;var f=g.substring(0,c),d=new e.Token(n,e.tokenize(u,t.grammar),"language-"+n,u),k=g.substring(c+p.length),m=[];f&&m.push.apply(m,walkTokens([f])),m.push(d),k&&m.push.apply(m,walkTokens([k])),"string"==typeof s?o.splice.apply(o,[i,1].concat(m)):s.content=m}}else s.content&&walkTokens(s.content)}return o}}}})}(e)}e.exports=markupTemplating,markupTemplating.displayName="markupTemplating",markupTemplating.aliases=[]},61028:function(e,t,n){"use strict";var a=n(93205);function tt2(e){e.register(a),e.languages.tt2=e.languages.extend("clike",{comment:/#.*|\[%#[\s\S]*?%\]/,keyword:/\b(?:BLOCK|CALL|CASE|CATCH|CLEAR|DEBUG|DEFAULT|ELSE|ELSIF|END|FILTER|FINAL|FOREACH|GET|IF|IN|INCLUDE|INSERT|LAST|MACRO|META|NEXT|PERL|PROCESS|RAWPERL|RETURN|SET|STOP|SWITCH|TAGS|THROW|TRY|UNLESS|USE|WHILE|WRAPPER)\b/,punctuation:/[[\]{},()]/}),e.languages.insertBefore("tt2","number",{operator:/=[>=]?|!=?|<=?|>=?|&&|\|\|?|\b(?:and|not|or)\b/,variable:{pattern:/\b[a-z]\w*(?:\s*\.\s*(?:\d+|\$?[a-z]\w*))*\b/i}}),e.languages.insertBefore("tt2","keyword",{delimiter:{pattern:/^(?:\[%|%%)-?|-?%\]$/,alias:"punctuation"}}),e.languages.insertBefore("tt2","string",{"single-quoted-string":{pattern:/'[^\\']*(?:\\[\s\S][^\\']*)*'/,greedy:!0,alias:"string"},"double-quoted-string":{pattern:/"[^\\"]*(?:\\[\s\S][^\\"]*)*"/,greedy:!0,alias:"string",inside:{variable:{pattern:/\$(?:[a-z]\w*(?:\.(?:\d+|\$?[a-z]\w*))*)/i}}}}),delete e.languages.tt2.string,e.hooks.add("before-tokenize",function(t){e.languages["markup-templating"].buildPlaceholders(t,"tt2",/\[%[\s\S]+?%\]/g)}),e.hooks.add("after-tokenize",function(t){e.languages["markup-templating"].tokenizePlaceholders(t,"tt2")})}e.exports=tt2,tt2.displayName="tt2",tt2.aliases=[]},64836:function(e){function _interopRequireDefault(e){return e&&e.__esModule?e:{default:e}}e.exports=_interopRequireDefault,e.exports.__esModule=!0,e.exports.default=e.exports}}]);