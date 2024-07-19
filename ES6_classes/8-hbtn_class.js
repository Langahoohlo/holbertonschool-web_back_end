export default class HolbertonClass {
    constructor(size, location) {
      this._size = size;
      this._location = location;
    }

    [Symbol.toPrimitive](dataType) {
        if (dataType === 'string') {
          return (`${this.location}`);
        } if (dataType === 'number') {
          return (`${this.size}`);
        }
        return (`${this.location}`);
      }
    
    get size() {
        return this._size;
    }
    set size(in_size) {
        this._size = in_size;
    }
    
    get location() {
        return this._location;
    }
    set location(in_location) {
        this._location = in_location;
    }
					
}