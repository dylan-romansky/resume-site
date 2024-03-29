import { Injectable } from '@angular/core';
import { ResIt } from './res-it';
import { Observable, of } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ResItService {
	httpOptions = {
		headers: new HttpHeaders({'Content-Type': 'application/json'})
	};
	//maybe instead of manually uncommenting, I
	//can make the scripts responsible for running
	//either a local dev deployment or a k8s
	//cluster deployment sed replace the uri with
	//the expected one

	//unless angular has conditional logic for
	//variables depending on if this is a dev or
	//prod environment
	private uri = 'http://localhost:5000/resume-item/'

	constructor(private http: HttpClient) { }

	getItems(): Observable<ResIt[]> {
		return this.http.get<ResIt[]>(this.uri).pipe(
				catchError(this.handleError<ResIt[]>('get ResIts', [])));
	}
	getItem(id: string): Observable<ResIt> {
		const url = `${this.uri}${id}`;
		return this.http.get<ResIt>(url).pipe(
				catchError(this.handleError<ResIt>('get ResIt')));
	}
	updateItem(resIt: ResIt): Observable<any> {
		return this.http.put(`${this.uri}${resIt.id}`, resIt, this.httpOptions).pipe(
				catchError(this.handleError<any>('update ResIt')));
	}
	addItem(resIt: ResIt): Observable<ResIt> {
		console.log("add");
		console.log(resIt);
		return this.http.post<ResIt>(this.uri, resIt, this.httpOptions).pipe(
				catchError(this.handleError<ResIt>('add ResIt')));
	}
	deleteItem(id: string): Observable<ResIt> {
		const url = `${this.uri}${id}`;
		return this.http.delete<ResIt>(url, this.httpOptions).pipe(
				catchError(this.handleError<ResIt>('delete ResIt')));
	}
	private handleError<T>(operation = 'operation', result?: T) {
		return (error: any): Observable<T> => {
			console.error(error);	//TODO: log to dedicated error server later
			return of(result as T);
		}
	}
}
