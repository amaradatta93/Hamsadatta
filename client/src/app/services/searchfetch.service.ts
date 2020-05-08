import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Observable, from } from 'rxjs';

import { Dash } from '../models/dash';

@Injectable({
  providedIn: 'root'
})
export class SearchfetchService {

  constructor(private http: HttpClient) {}

  getSearchedPosts(search_params: string): Observable<Dash[]> {
    let searchPostUrl = `http://127.0.0.1:8000/api/user-dashboard/search?search_param=${search_params}`;
    return this.http.get<Dash[]>(searchPostUrl);
  }

}
