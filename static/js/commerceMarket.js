Array.prototype.split = function(chunks){
    response = [];
    aux_array = [];
    for(var i = 0; i <  this.length; i++){
        if(aux_array.length < chunks){
            aux_array.push(this[i]);
        }else{
            response.push(aux_array);
            aux_array = [];
            aux_array.push(this[i])
        }
    }
    if(aux_array.length > 0){
        response.push(aux_array);
    } 
    return response;

}


angular.module("commerceMarket", [])
.controller("commerceMarketController", function($scope){
    var market = this;
    market.commerces = data;
    market.categories = categories;
    market.pack_commerces = market.commerces.split(3);
    market.neighborhoods = neighborhoods;
    market.pack_neighborhoods = market.neighborhoods.split(3);
    market.MEDIA_URL = MEDIA_URL;
    $scope.searchValue = "";
    $("#searchForm").submit(function(){
        return false;
    });
    market.categories_filter = [];
    market.selected_categories = [];
    $scope.$watch("searchValue", function(){
        if($scope.searchValue !== undefined){
            var value = $scope.searchValue.toLowerCase();
            if(market.selected_categories.length > 0){
                var aux = [];
                angular.forEach(market.commerces, function(commerce){
                    if(market.selected_categories.indexOf(commerce.category) >= 0 && (commerce.name.toLowerCase().split(value).length > 1 || commerce.description.toLowerCase().split(value).length > 1)){
                        aux.push(commerce);
                    }

                });
                market.pack_commerces = aux.split(3);
            }else{
                var aux = [];
                angular.forEach(market.commerces, function(commerce){
                    if(commerce.name.toLowerCase().split(value).length > 1 || commerce.description.toLowerCase().split(value).length > 1){
                        aux.push(commerce);
                    }

                });

                market.pack_commerces = aux.split(3);
            }
        }
    })
    market.filter = function(cate){
        if(cate.selected && cate.pk != 0){
            angular.forEach(market.categories, function(category){
                if(category.pk != cate.pk){
                    category.selected = false;
                }
            })
            aux = []; 
            angular.forEach(market.commerces, function(commerce){
                if(commerce.category == cate.pk){
                    aux.push(commerce);
                }
            })
            
            market.pack_commerces = aux.split(3);
        }else{
            angular.forEach(market.categories, function(category){
                if(category.pk > 0){
                    category.selected = false;
                }else{
                    category.selected = true;
                }
            })    
            market.pack_commerces = market.commerces.split(3);
        }

    }
    market.filter_category = function(cate){
        if(market.selected_categories.indexOf(cate.pk) == -1){
            market.selected_categories.push(cate.pk);
        }else{
            var aux = [];
            angular.forEach(market.selected_categories, function(cat){
                if(cat != cate.pk){
                    aux.push(cat)
                }
            });
            market.selected_categories = aux;

        }
        if($scope.searchValue === undefined){
            if(market.selected_categories.length > 0){
                var aux = [];
                angular.forEach(market.commerces, function(commerce){
                    if(market.selected_categories.indexOf(commerce.category) >= 0){
                        aux.push(commerce);
                    }

                });
                market.pack_commerces = aux.split(3);
            }else{
                market.pack_commerces = market.commerces.split(3);
            }
        }else{
            var value = $scope.searchValue.toLowerCase();
            if(market.selected_categories.length > 0){
                var aux = [];
                angular.forEach(market.commerces, function(commerce){
                    if(market.selected_categories.indexOf(commerce.category) >= 0 && (commerce.name.toLowerCase().split(value).length > 1 || commerce.description.toLowerCase().split(value).length > 1)){
                        aux.push(commerce);
                    }

                });
                market.pack_commerces = aux.split(3);
            }else{
                var aux = [];
                angular.forEach(market.commerces, function(commerce){
                    if(commerce.name.toLowerCase().split(value).length > 1 || commerce.description.toLowerCase().split(value).length > 1){
                        aux.push(commerce);
                    }

                });

                market.pack_commerces = aux.split(3);
            }       
        }
    }
})