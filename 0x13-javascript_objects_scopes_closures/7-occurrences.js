#!/usr/bin/node

exports.nbOccurences = function (list, searchElement){
    let count = 0;
    list.forEach(Element => {
        if (Element === searchElement) count ++;
    });
    return count;
}
