import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';
import { ResIt } from './res-it';

@Injectable({
  providedIn: 'root'
})
export class InMemoryDataService implements InMemoryDbService {
	createDb() {
		const resume: ResIt[] = [
			{id: '1', name: 'test1', title: 'test',
				startdate: "6/7/2022", enddate: '6/7/2069',
				content: 'test', type: 'job'},
			{id: '2', name: 'test2', title: '',
				startdate: '6/7/2018', enddate: '6/7/2020',
				content: 'test', type: 'edu'}
		];
		return {resume};
	}

	genID(resIts: ResIt[]) {
		return (resIts.length > 0 ? Math.max(...resIts.map(resIt => parseInt(resIt.id))) + 1 : 1).toString();
	}
}
