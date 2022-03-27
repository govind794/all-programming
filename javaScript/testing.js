// 👉️ Not Supported in IE 6-11
const array = [
    'https://staging.in2tive.xyz/login#/',
    'https://staging.in2tive.xyz/login#/app',
    'https://staging.in2tive.xyz/login#/pipelines',
    'https://staging.in2tive.xyz/login#/env',
    'https://staging.in2tive.xyz/login#/cluster',
    'https://staging.in2tive.xyz/login#/provider',
    'https://staging.in2tive.xyz/login#/member',
    'https://staging.in2tive.xyz/login#/settings/config'
  ];
const substring = '#/cluster';

const match = array.find(element => {
  if (element.includes(substring)) {
      return true;
  }
});

console.log( array.indexOf(match));
