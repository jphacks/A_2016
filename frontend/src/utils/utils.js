export function getSearchObj(searchStr) {
  if (!searchStr) return {};
  return searchStr
    .substr(1)
    .split('&')
    .reduce((acc, cur) => {
      acc[cur.split('=')[0]] = cur.split('=')[1];
      return acc;
    }, {});
}
